from django.contrib import admin
from . import models

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "due_date")
    #list_display = ("title",  "date", "category", "content", "Todo")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(models.TodoList, TodoListAdmin)
admin.site.register(models.Category, CategoryAdmin)

# admin.site.register(Category)

# admin.site.register(BrTodoListand)