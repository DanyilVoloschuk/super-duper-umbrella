import {Component, OnInit} from '@angular/core';
import {UserService} from '../services/user.service';
import {User} from '../interfaces/user';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: [
    '../app.component.css',
    './users.component.css']
})
export class UsersComponent implements OnInit {
  users: User[] | undefined;

  constructor(private usersService: UserService, private sanitizer: DomSanitizer) {
  }

  getUsersList() {
    this.usersService.getUsers()
      .subscribe((data: any) => {
        this.users = data;
      });
  }

  public getSantizeBase64Url(url: string) {
    return this.sanitizer.bypassSecurityTrustUrl('data:image/png;base64, ' + url);
  }

  ngOnInit(): void {
    this.getUsersList();
  }

}
