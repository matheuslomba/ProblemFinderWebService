import axios from 'axios';

export const api = axios.create({
    baseURL:"http://localhost:8080/"
})

export const apiMain = axios.create({
    baseURL:"http://localhost:5000/"
})