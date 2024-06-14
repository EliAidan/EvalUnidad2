<template>

  <div class="flex justify-center items-center h-screen bg-indigo-700">
    <div class="w-full bg-indigo-100 rounded p-5" style="max-width: 50rem;">
      <!-- Pestañas -->
      <div class="flex mb-4">
        <button @click="mostrarPaso(1)"
          :class="{ 'bg-indigo-700 text-white': pasoActivo === 1, 'bg-gray-300': pasoActivo !== 1 }"
          class="w-1/3 py-2 rounded-tl-lg focus:outline-none">Paso 1</button>
        <button @click="mostrarPaso(2)"
          :class="{ 'bg-indigo-700 text-white': pasoActivo === 2, 'bg-gray-300': pasoActivo !== 2 }"
          class="w-1/3 py-2 focus:outline-none">Paso 2</button>
        <button @click="mostrarPaso(3)"
          :class="{ 'bg-indigo-700 text-white': pasoActivo === 3, 'bg-gray-300': pasoActivo !== 3 }"
          class="w-1/3 py-2 rounded-tr-lg focus:outline-none">Paso 3</button>
      </div>
      <!-- Contenido del paso -->
      <div>
        <div v-if="pasoActivo === 1">
          <form-paso-1 />
        </div>
        <div v-if="pasoActivo === 2">
          <form-paso-2 />
        </div>
        <div v-if="pasoActivo === 3">
          <form-paso-3 />
        </div>
      </div>

      <button @click="anteriorPaso" v-if="pasoActivo > 1" class="w-1/2 bg-gray-700 hover:bg-pink-700 text-white font-bold py-2 px-4 mb-6 rounded float-left">
        Anterior
      </button>
      <button @click="siguientePaso" v-if="pasoActivo < 3" class="w-1/2 bg-indigo-700 hover:bg-pink-700 text-white font-bold py-2 px-4 mb-6 rounded float-right">
        Siguiente
      </button>
      <button @click="enviarFormulario" v-if="pasoActivo === 3" class="w-full bg-indigo-700 hover:bg-pink-700 text-white font-bold py-2 px-4 mb-6 rounded">
        Registrar usuario
      </button>

      <button>
        <RouterLink to="/login">
          <a class="text-indigo-700 hover:text-pink-700  float-right" href="#">Regresar</a>
        </RouterLink>
      </button>


      

      
    </div>
  </div>
</template>

<script>
import FormPaso1 from '../components/datosPaciente.vue';
import FormPaso2 from '../components/datosContacto.vue';
import FormPaso3 from '../components/datosMedicos.vue';

export default {
  components: {
    FormPaso1,
    FormPaso2,
    FormPaso3
  },
  data() {
    return {
      pasoActivo: 1
    }
  },
  methods: {
    mostrarPaso(paso) {
      this.pasoActivo = paso;
    },
    siguientePaso() {
      if (this.pasoActivo < 3) {
        this.pasoActivo++;
      }
    },
    anteriorPaso() {
      if (this.pasoActivo > 1) {
        this.pasoActivo--;
      }
    },
    enviarFormulario() {
      // Aquí puedes enviar el formulario completo
    }
  }
}
</script>

<style scoped>
/* Estilos específicos del componente */
</style>
