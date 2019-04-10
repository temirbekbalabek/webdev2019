import { TodoFrontPage } from './app.po';

describe('todo-front App', function() {
  let page: TodoFrontPage;

  beforeEach(() => {
    page = new TodoFrontPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
