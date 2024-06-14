<template>
    <div class="bg-gray-900 text-white p-8 rounded-lg">
        <div v-if="mensaje">{{ mensaje }}</div>
        <h1>Insertar Datos</h1>
        <form @submit.prevent="insertarDatos" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
                <label for="nombres" class="block mb-2">Nombre(s)</label>
                <input type="text" id="nombres" v-model="nombres"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="apellidop" class="block mb-2">Apellido Paterno</label>
                <input type="text" id="apellidop" v-model="apellidop"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="apellidom" class="block mb-2">Apellido Materno</label>
                <input type="text" id="apellidom" v-model="apellidom"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="sexo" class="block mb-2">Sexo:</label>
                <select id="sexo" v-model="sexo" required class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
                    <option value="">Seleccionar</option>
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                </select>
            </div>

            <div>
                <label for="fecha_nacimiento" class="block mb-2">Fecha de Nacimiento:</label>
                <input type="date" id="fecha_nacimiento" v-model="fechaNacimiento"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="edad_anos" class="block mb-2">Edad (años):</label>
                <input type="number" id="edad_anos" v-model="edadAnos"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="peso" class="block mb-2">Peso (kg):</label>
                <input type="number" id="peso" step="0.1" v-model="peso"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="longitud" class="block mb-2">Longitud (cm):</label>
                <input type="number" id="longitud" step="0.1" v-model="longitud"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="perimetro_craneal" class="block mb-2">Perímetro Craneal (cm):</label>
                <input type="number" id="perimetro_craneal" step="0.1" v-model="perimetroCraneal"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="temperatura" class="block mb-2">Temperatura (°C):</label>
                <input type="number" id="temperatura" step="0.1" v-model="temperatura"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="frecuencia_respiratoria" class="block mb-2">Frecuencia Respiratoria:</label>
                <input type="number" id="frecuencia_respiratoria" v-model="frecuenciaRespiratoria"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="frecuencia_cardiaca" class="block mb-2">Frecuencia Cardíaca:</label>
                <input type="number" id="frecuencia_cardiaca" v-model="frecuenciaCardiaca"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="presion_arteria_sistolica" class="block mb-2">Presión Arterial Sistólica:</label>
                <input type="number" id="presion_arteria_sistolica" v-model="presionArterialSistolica"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="presion_arteria_diastolica" class="block mb-2">Presión Arterial Diastólica:</label>
                <input type="number" id="presion_arteria_diastolica" v-model="presionArterialDiastolica"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>
            <div>
                <label for="observaciones" class="block mb-2">Observaciones:</label>
                <textarea id="observaciones" v-model="observaciones"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white"></textarea>
            </div>

            <div>
                <label for="fecha_ultima_cita" class="block mb-2">Fecha de la última cita:</label>
                <input type="date" id="fecha_ultima_cita" v-model="fecha_ultima_cita"
                    class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div class="bg-gray-900 text-white  rounded-lg">

                <div v-for="(vacuna, index) in vacunas" :key="index">
                    <label :for="'vacuna_' + index" class="block mb-2">Vacuna {{ index + 1 }}:</label>
                    <input type="text" :id="'vacuna_' + index" :value="vacuna" @input="actualizarVacuna($event, index)"
                        class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
                    <button type="button" @click="eliminarVacuna(index)" v-if="index > 0"
                        class="text-white bg-red-500 py-1 px-2 rounded-md mt-4">Eliminar</button>
                </div>
                <button type="button" @click="agregarVacuna"
                    class="text-white bg-blue-500 py-1 px-2 rounded-md mt-4">Agregar
                    Vacuna</button>
            </div>
           
           



        </form>
        <div class="md:col-span-4 w-full mt-8 flex justify-center items-center">
            <button type="submit"
                class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md">Insertar</button>
        </div>
        
    </div>
    
</template>


<script>
export default {
    data() {
        return {
            nombres: '',
            apellidop: '',
            apellidom: '',
            sexo: '',
            fechaNacimiento: '',
            fecha_ultima_cita: '',
            edadAnos: null,
            peso: null,
            longitud: null,
            perimetroCraneal: null,
            temperatura: null,
            frecuenciaRespiratoria: null,
            frecuenciaCardiaca: null,
            presionArterialSistolica: null,
            presionArterialDiastolica: null,
            vacunas: [''],
            citas: [''],
            examenes: [''],
            observaciones: '',
            mensaje: ''
        };
    },
    methods: {
        insertarDatos() {
            const data = {
                nombres: this.nombres,
                apellidop: this.apellidop,
                apellidom: this.apellidom,
                sexo: this.sexo,
                fecha_nacimiento: this.fechaNacimiento,
                fecha_ultima_cita: this.fecha_ultima_cita,
                edad_anos: this.edadAnos,
                peso: this.peso,
                longitud: this.longitud,
                perimetro_craneal: this.perimetroCraneal,
                temperatura: this.temperatura,
                frecuencia_respiratoria: this.frecuenciaRespiratoria,
                frecuencia_cardiaca: this.frecuenciaCardiaca,
                presion_arteria_sistolica: this.presionArterialSistolica,
                presion_arteria_diastolica: this.presionArterialDiastolica,
                vacunas_administradas: this.vacunas.filter(vacuna => vacuna.trim() !== ''),
                citas: this.citas.filter(cita => cita.trim() !== ''),
                examenes_medicos_realizados: this.examenes.filter(examen => examen.trim() !== ''),
                observaciones: this.observaciones
            };

            fetch('http://127.0.0.1:8000/hospital/api/mongo/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(response => {
                    if (response.ok) {
                        this.mensaje = 'Datos insertados correctamente.';
                        this.limpiarCampos();
                    } else {
                        this.mensaje = 'Error al insertar los datos.';
                    }
                })
                .catch(error => {
                    this.mensaje = 'Error al insertar los datos.';
                    console.error(error);
                });
        },
        agregarVacuna() {
            this.vacunas.push('');
        },
        eliminarVacuna(index) {
            this.vacunas.splice(index, 1);
        },
        actualizarVacuna(event, index) {
            this.vacunas[index] = event.target.value;
        },
        agregarCita() {
            this.citas.push('');
        },
        eliminarCita(index) {
            this.citas.splice(index, 1);
        },
        actualizarCita(event, index) {
            this.citas[index] = event.target.value;
        },
        agregarExamen() {
            this.examenes.push('');
        },
        eliminarExamen(index) {
            this.examenes.splice(index, 1);
        },
        actualizarExamen(event, index) {
            this.examenes[index] = event.target.value;
        },
        limpiarCampos() {
            this.nombres = '',
                this.apellidop = '',
                this.apellidom = '',
                this.sexo = '',
                this.fechaNacimiento = '',
                this.fecha_ultima_cita = '',
                this.edadAnos = null;
            this.peso = null;
            this.longitud = null;
            this.perimetroCraneal = null;
            this.temperatura = null;
            this.frecuenciaRespiratoria = null;
            this.frecuenciaCardiaca = null;
            this.presionArterialSistolica = null;
            this.presionArterialDiastolica = null;
            this.vacunas = [''];
            this.examenes = [''];
            this.citas = [''];
            this.observaciones = '';
        }
    }
};
</script>

<style scoped>
/* Estilos CSS específicos del componente */
</style>