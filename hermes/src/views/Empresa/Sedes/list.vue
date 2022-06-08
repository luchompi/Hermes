<template>
    <div class="SedeList">
        <h1>Listado de Sedes 
            <a name="" id="" class="btn btn-primary" href="#" role="button">Crear nuevo</a> 

        </h1>
        <table class="table table-striped table-hover">
              <thead>
                <tr>
                  <th scope="col">#</th>
                  <th scope="col">Sede</th>
                  <th scope="col">Opciones</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="row in data" :key="row.id">
                  <th scope="row">{{row.id}}</th>
                  <td>{{row.sede}}</td>
                  <td>
                    <div class="btn-group" role="group" aria-label="Basic example">
                    <button type="submit" class="btn btn-warning">Editar</button>
                    <a v-on:click="borrarSede(row.id)" class="btn btn-danger">Borrar</a>
            </div>
                  </td>
                </tr>
              </tbody>
        </table>
    </div>
</template>
<script>
import {getAPI} from '@/axios-api'
export default {
    name: 'SedeList',
    data() {
        return {
            data:[]
        }
    },
    created() {
        fetch('http://sigma-beta.herokuapp.com/empresa/sedes/api/v1.0/').then(response=>response.json())
        .then(dataResponse=>{
          this.data = dataResponse;
          console.log(dataResponse)
        })
    },
    methods: {
      borrarSede (id) {
        getAPI.delete('/empresa/sedes/api/v1.0/'+id)
         .then(response=>response.data)
        .then(dataResponse=>{
          console.log(dataResponse)
        })
        
      }
    }

}
</script>