import { NgModule } from '@angular/core';
import { TextSummarizationComponent } from './text-summarization.component';
import { RouterModule } from '@angular/router';
import { routes } from './text-summarization.routes';
import { MaterialModule } from '../../shared/material.module';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

 @NgModule({
    declarations: [
        TextSummarizationComponent
    ],
    imports: [
        MaterialModule,
        FormsModule,
        RouterModule.forChild(routes),
        CommonModule
    ],
 })
 export class TextSummarizationModule {}