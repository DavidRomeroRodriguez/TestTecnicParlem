import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Customer } from './model-interfaces/customer';
import { Product } from './model-interfaces/product';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'parlem-front';
  customers: Customer[] = [];
  products: Product[] = [];

  constructor(private http: HttpClient) {
    this.title = 'parlem-front';
    this.http.get('http://localhost:5000/api/customer/all').subscribe((customers: Customer[]) => {
      this.customers = customers;
      console.log('customers', this.customers);
    });
    this.http.get('http://localhost:5000/api/product/all').subscribe((products: Product[]) => {
      this.products = products;
      console.log('products', this.products);
    });
  }
}
