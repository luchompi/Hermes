<template>
<div class="NewSede">
    <h1>Crear Nueva Sede</h1>
    <div class="container-fluid">
        <form class="form-group" v-on:submit.prevent="agregarRegistro">
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Nombre de la sede</span>
                <input type="text" class="form-control" v-model="sede" placeholder="ej: Riohacha" aria-label="Username" aria-describedby="basic-addon1">
            </div>
            <div class="btn-group" role="group" aria-label="Basic example">
                <button type="submit" class="btn btn-primary">Guardar</button>
                <router-link :to="{name:'SedeList'}" class="btn btn-danger">Cancelar</router-link>
            </div>
        </form>
    </div>
</div>

</template>
<script>
import {getAPI} from '@/axios-api'
export default {
    name:'NewSede',
    data(){
        return{
            sede:'',
        }
    },
    methods:{
    agregarRegistro(){
        console.log(this.sede);
        var data_sede = {
            'sede':this.sede
        }
        getAPI.post('/empresa/sedes/api/v1.0/', data_sede)
        .then(response=>response.data)
        .then(dataResponse=>{
          window.location.href="empresa/sedes/"
        })
        
    }, 
    },
}
</script>