import { Component, OnInit } from '@angular/core';
import { ITaskList, ITask } from '../shared/models/models';
import { ProviderService } from '../shared/services/provider.service';


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {
  public task_lists: ITaskList[] = [];
  public tasks: ITask[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    });
  }
  getListOfTasks(task_list: ITaskList) {
    this.provider.getTasks(task_list.id).then(res => {this.tasks = res; });
  }

}