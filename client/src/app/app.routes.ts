import { Routes } from '@angular/router';

export const routes: Routes = [
    {
        path: 'text-summarization',
        loadChildren: () => import('./features/text-summarization/text-summarization.module').then(m =>
             m.TextSummarizationModule) 
    }
];
