<script setup>

import {ref, computed} from 'vue';
import argentina from '../assets/images/argentina.png'
import uruguay from '../assets/images/uruguay.png'
import brasil from '../assets/images/brasil.png'
import chile from '../assets/images/chile.png'
 // Variable stática

const paisesComputados = [
  {
    bandera: argentina,
    pais:'Argentina',
    capital: 'Buenos Aires',
    moneda: 'Peso Argentino',
  },

  {
    bandera: uruguay,
    pais: 'Uruguay',
    capital: 'Montevideo',
    moneda: 'Peso uruguayo',
  },

  {
    bandera: brasil,
    pais: 'Brasil',
    capital: 'Brasilia',
    moneda: 'Real',
  },

  {
    bandera: chile,
    pais: 'Chile',
    capital: 'Santiago de Chile',
    moneda: 'Sol',
  },
]

const contadorPaises = ref(0);
const totalPaises = paisesComputados.length;

const siguiente = () => {
  contadorPaises.value++;
  if (contadorPaises.value >= totalPaises) {
    contadorPaises.value = 0;
  }
}

const anterior = () => {
  contadorPaises.value--;
  if (contadorPaises.value <=  0) {
    contadorPaises.value = totalPaises - 1;
  }
}

const imagen = computed(()=>{
  return paisesComputados[contadorPaises.value].bandera
})
</script>

<template>
  <div class="card" style="width: 18rem;">
      <img :src="imagen" class="card-img-top" alt= "#">
        <div class="card-body">
          <h5 class="card-title"> {{ paisesComputados[contadorPaises].pais }}</h5>
          <p class="card-text"> {{ paisesComputados[contadorPaises].capital }}</p>
          <p class="card-text"> {{ paisesComputados[contadorPaises].moneda }}</p>
          <p class="text-secondary text-center"> {{contadorPaises + 1}} de {{totalPaises}}</p>
          <button class="btn btn-sm btn-success" @click="anterior" >Anterior</button>
          <button class="btn btn-sm btn-success" @click="siguiente" >Siguiente</button>
        </div>
    </div>
</template>

<style scoped>
</style>