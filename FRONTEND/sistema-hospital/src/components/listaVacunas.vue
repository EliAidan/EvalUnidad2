<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Registro de Vacunas</h1>

    <!-- Tabla de registros de vacunas -->
    <table class="table-auto w-full">
      <thead>
        <tr class="bg-gray-200">
          <th class="px-4 py-2">ID del paciente</th>
          <th class="px-4 py-2">Nombre del paciente</th>
          <th class="px-4 py-2">Nombre de los padres</th>
          <th class="px-4 py-2">Nombre de la vacuna</th>
          <th class="px-4 py-2">Fecha de administración</th>
          <th class="px-4 py-2">Edad del niño/a</th>
          <th class="px-4 py-2">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(registro, index) in registros" :key="index" class="hover:bg-gray-100">
          <td class="border px-4 py-2">{{ registro.id }}</td>
          <td class="border px-4 py-2">{{ registro.nombre }}</td>
          <td class="border px-4 py-2">{{ registro.nombrePadres }}</td>
          <td class="border px-4 py-2">{{ registro.nombreVacuna }}</td>
          <td class="border px-4 py-2">{{ registro.fecha }}</td>
          <td class="border px-4 py-2">{{ registro.edad }}</td>
          <td class="border px-4 py-2">
            <button @click="eliminarRegistro(index)" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded mr-2">Eliminar</button>
            <button @click="editarRegistro(index)" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      registros: [
        { id: 1, nombre: 'Juan Pérez', nombrePadres: 'Luis Pérez y María García', nombreVacuna: 'BCG', fecha: '2023-01-15', edad: 0 },
        { id: 2, nombre: 'María García', nombrePadres: 'Carlos García y Ana López', nombreVacuna: 'Hepatitis B', fecha: '2023-02-02', edad: 0 },
        { id: 3, nombre: 'Pedro López', nombrePadres: 'Javier López y Laura Martínez', nombreVacuna: 'Pentavalente', fecha: '2023-03-10', edad: 2 },
      ]
    }
  },
  methods: {
    eliminarRegistro(index) {
      this.registros.splice(index, 1);
    },
    editarRegistro(index) {
      // Puedes implementar la lógica para editar un registro aquí si lo deseas
    }
  }
}
</script>

<style scoped>
/* Estilos específicos del componente */
</style>
