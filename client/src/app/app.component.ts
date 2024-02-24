import { Component, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'text-summarization';
  hideFrontPage = false;

  constructor(private readonly router: Router){
  
  }
  ngOnInit(): void {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        this.hideFrontPage = !(event.url === '/');
      }
    });
  }

  goToSummarize(){
    this.hideFrontPage = true
    this.router.navigate(['text-summarization']);
  }
    
  
}
