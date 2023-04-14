import os
import json
from datetime import datetime

class TodoItem:
    def __init__(self, title, description, importance, due_date):
        self.title = title
        self.description = description
        self.importance = importance
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.is_completed = False

    def mark_as_completed(self):
        self.is_completed = True

    def to_dict(self):
        return {
            'title': self.title,
            'description': self.description,
            'importance': self.importance,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'is_completed': self.is_completed
        }

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def view_items(self):
        sorted_items = sorted(self.items, key=lambda x: (not x.is_completed, x.importance, x.due_date))
        for item in sorted_items:
            status = 'Completed' if item.is_completed else 'Not Completed'
            print(f'{item.title} - {item.description} - {item.importance} - {item.due_date.strftime("%Y-%m-%d")} - {status}')

    def save_to_file(self, file_path):
        items_dict = [item.to_dict() for item in self.items]
        with open(file_path, 'w') as f:
            json.dump(items_dict, f)

    def load_from_file(self, file_path):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                items_dict = json.load(f)
            for item_dict in items_dict:
                item = TodoItem(item_dict['title'], item_dict['description'], item_dict['importance'], item_dict['due_date'])
                item.is_completed = item_dict['is_completed']
                self.add_item(item)

todo_list = TodoList()

while True:
    print('1. Add item')
    print('2. Remove item')
    print('3. View items')
    print('4. Mark item as completed')
    print('5. Save to file')
    print('6. Load from file')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        title = input('Enter title: ')
        description = input('Enter description: ')
        importance = int(input('Enter importance (1-5): '))
        due_date = input('Enter due date (YYYY-MM-DD): ')
        item = TodoItem(title, description, importance, due_date)
        todo_list.add_item(item)
        print('Item added.')

    elif choice == '2':
        title = input('Enter title: ')
        for item in todo_list.items:
            if item.title == title:
                todo_list.remove_item(item)
                print('Item removed.')
                break

    elif choice == '3':
        todo_list.view_items()

    elif choice == '4':
        title = input('Enter title: ')
        for item in todo_list.items:
            if item.title == title:
                item.mark_as_completed()
                print('Item marked as completed.')
                break

    elif choice == '5':
        file_path = input('Enter file path: ')
        todo_list.save_to_file(file_path)
        print('Items saved to file.')

    elif choice == '6':
        file_path = input('Enter file path: ')
        todo_list.load_from_file(file_path)
        print('Items loaded from file.')

    elif choice == '7':
        break

    else:
        print('Invalid choice. Please try again.')

