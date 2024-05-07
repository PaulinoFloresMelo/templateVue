import { defineStore } from "pinia";

export const useTodo = defineStore('todo', {
    state: ()=>({
        todoList:[],
        id:0
    }),

    getters:{
        totalTodo:(state)=>{
            return state.todoList.length
        },
        totalCompleted:(state)=>{
            const total = state.todoList.filter(item => item.completed)
            return total.length
        }
    },

    actions:{
        addTodo(task){
            const date = new Date()
            const newTask = {id:this.id++, task, completed:false, date}
            this.todoList.push(newTask)
        },

        toggleTodo(id){
            const task = this.todoList.find(item => item.id === id)
            if (task) {
                task.completed = !task.completed
            }
        },
        deleteTodo(id){
            this.todoList = this.todoList.filter(item => item.id !== id)
        }
    }
})