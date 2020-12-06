import {Injectable} from '@angular/core';
import {HttpClient, HttpParams} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) {
  }

  private ip = 'http://127.0.0.1:8000/';

  getUsers(): Observable<any> {
    return this.http.get<any>(this.ip + 'users/users_list/');
  }

  orderItem(login: string, password: string, item_id: bigint): Observable<any> {
    return this.http.post<any>(this.ip + `goods/add_item_to_user/${item_id}`, {login: login, password: password});
  }
}
