import { Component, OnInit } from '@angular/core';
import { SummarizationMethods } from './enums/summarization-methods';
import { Summarize } from './models/summarize.model';
import { TextSummarizationService } from './services/text-summarization.service';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
    selector: 'text-summarization-app',
    templateUrl: './text-summarization.component.html',
    styleUrls: ['./text-summarization.component.scss']
})
export class TextSummarizationComponent implements OnInit{

    inputText:string='';
    summarizedText:string='';
    originalText:string='';
    selectedMethod: string = '';
    summarizationMethods: string[];
    isLoading: boolean = false;
    
    constructor(
        private readonly service: TextSummarizationService,
        private snackBar: MatSnackBar){
        this.summarizationMethods = Object.values(SummarizationMethods);
    }

    ngOnInit(): void {
        this.inputText = `Artificial intelligence is human like intelligence. It is the study of intelligent artificial agents. Science and engineering to produce intelligent machines. Solve problems and have intelligence. Related to intelligent behavior. Developing of reasoning machines. Learn from mistakes and successes. Artificial intelligence is related to reasoning in everyday situations.`;
    }

    summarize(){
        this.isLoading = true;
        const params : Summarize = {
            text: this.inputText,
            method: this.selectedMethod 
        };

        this.service.summarize(params)
        .then(response => {
            this.summarizedText = '';
            this.originalText = '';
            response.sentence_list.forEach(sentence => {
                if (response.best_sentences.includes(sentence)) {
                    this.originalText += ` <mark>${sentence}</mark>`;

                    if(response.method !== 'GPT'){
                        this.summarizedText += ` ${sentence}`;
                    }
                } else {
                    this.originalText += ` ${sentence}`;
                }
            });

            if(response.method === 'GPT'){
                this.summarizedText = response.best_sentences.join(' ');
            }

            this.openSnackBar('successfully summarized text', 'success-snackbar');
        })
        .catch(error => {
            this.openSnackBar(error.statusText, 'error-snackbar');
            console.log(error);
        })
        .finally(() => {
            this.isLoading = false;
        });
    }

    openSnackBar(message: string, panelClass:string) {
        this.snackBar.open(message, '', {
            duration: 2000,
            panelClass: [panelClass]
        });
      }
}