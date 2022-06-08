import axios from 'axios'

const getAPI = axios.create({
    baseURL: 'http://sigma-beta.herokuapp.com/',
    timeout: 1000,
    headers: {
        'Content-Type': 'application/json'
    }
})
export {getAPI}