<template>
	<h1>Editar Sede</h1>
	<div class="container-fluid">
        <form class="form-group" v-on:submit.prevent="actualizarRegistro">
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Nombre de la sede</span>
                <input type="text" class="form-control" v-model="sede" aria-label="Username" aria-describedby="basic-addon1">
            </div>
            <div class="btn-group" role="group" aria-label="Basic example">
                <button type="submit" class="btn btn-success">Actualizar</button>
                <router-link :to="{name:'SedeList'}" class="btn btn-danger">Cancelar</router-link>
            </div>
        </form>
    </div>
</template>
<script>
	import {getAPI} from '@/axios-api'
export default {
    name: 'EditSede',
    data() {
        return {
            sede:'',
            
        }
    },
    created(){
    	this.getQueryset()
    },
    methods:{
    	getQueryset(){
    		getAPI.get('/empresa/sedes/api/v1.0/'+this.$route.params.id)
    		.then(response=>response.data)
        .then(dataResponse=>{
        	this.sede=dataResponse.sede
        	
        })
    	},
    	actualizarRegistro(){
    		var data_sede = {
    			'id':this.$route.params.id,
            'sede':this.sede
        }
        getAPI.put('/empresa/sedes/api/v1.0/'+this.$route.params.id+'/', data_sede)
        .then(response=>response.data)
        .then(dataResponse=>{
          window.location.href="empresa/sedes/"
        })
    	}
    }
    

}
</script>