import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ZCO50248Component } from './zco50248.component';

describe('ZCO50248Component', () => {
  let component: ZCO50248Component;
  let fixture: ComponentFixture<ZCO50248Component>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ZCO50248Component ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ZCO50248Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
