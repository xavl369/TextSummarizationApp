import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environments';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Summarize } from '../models/summarize.model';
import { firstValueFrom } from 'rxjs';
import { SummarizeResult } from '../models/summarie-result';

@Injectable({
    providedIn: 'root'
})
export class TextSummarizationService {

    private readonly baseUrl = environment.textSummarizationUrl;
    private readonly apiKey = environment.summarizationAPIKey;

    constructor(private readonly httpClient: HttpClient){}

    summarize(params : Summarize) : Promise<SummarizeResult>{
        const headers = new HttpHeaders().set('Authorization', this.apiKey);
        return firstValueFrom(this.httpClient.post<SummarizeResult>(this.baseUrl, params, { headers:headers }));
    }

}