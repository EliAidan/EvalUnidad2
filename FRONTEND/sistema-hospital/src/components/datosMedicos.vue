<template>
 <div>
                <label for="observaciones" class="block mb-2">Observaciones:</label>
                <textarea id="observaciones" v-model="observaciones" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white"></textarea>
            </div>

            <div>
                <label for="tipoNacimiento" class="block mb-2">Tipo de Nacimiento:</label>
                <select id="tipoNacimiento" v-model="tipoNacimiento" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
                    <option value="1">Normal</option>
                    <option value="0">Cesárea</option>
                </select>
            </div>

            <div>
                <label for="frecuenciaCardiaca" class="block mb-2">Frecuencia Cardíaca:</label>
                <input type="number" id="frecuenciaCardiaca" v-model="frecuenciaCardiaca" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="temperatura" class="block mb-2">Temperatura (°C):</label>
                <input type="number" id="temperatura" v-model="temperatura" step="0.01" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="presionArterialSistolica" class="block mb-2">Presión Arterial Sistólica:</label>
                <input type="number" id="presionArterialSistolica" v-model="presionArterialSistolica" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="presionArterialDiastolica" class="block mb-2">Presión Arterial Diastólica:</label>
                <input type="number" id="presionArterialDiastolica" v-model="presionArterialDiastolica" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

</template>

<script>
/* eslint-disable */
export default {
    data() {
        return {
            sexo: '',
            fechaNacimiento: '',
            horaNacimiento: '',
            lugarNacimiento: '',
            peso: null,
            longitud: null,
            nombrePadre: '',
            nombreMadre: '',
            telefonoContacto: '',
            emailContacto: '',
            observaciones: '',
            tipoNacimiento: '',
            frecuenciaCardiaca: null,
            temperatura: null,
            presionArterialSistolica: null,
            presionArterialDiastolica: null,
            message: ''
        }
    },
    methods: {
        submitForm() {
            let data = {
                sexo: this.sexo,
                fecha_nacimiento: this.fechaNacimiento,
                hora_nacimiento: this.horaNacimiento,
                lugar_nacimiento: this.lugarNacimiento,
                peso: this.peso,
                longitud: this.longitud,
                nombre_padre: this.nombrePadre,
                nombre_madre: this.nombreMadre,
                telefono_contacto: this.telefonoContacto,
                email_contacto: this.emailContacto,
                observaciones: this.observaciones,
                tipo_nacimiento: this.tipoNacimiento,
                frecuencia_cardiaca: this.frecuenciaCardiaca,
                temperatura: this.temperatura,
                presion_arterial_sistolica: this.presionArterialSistolica,
                presion_arterial_diastolica: this.presionArterialDiastolica
            };

            fetch('http://127.0.0.1:8000/hospital/api/nacimientos/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Hubo un problema al registrar el bebé.');
                    }
                    return response.json();
                })
                .then(data => {
                    this.message = "¡Bebé registrado exitosamente!";
                    // Limpiar los campos del formulario después del registro exitoso
                    this.resetForm();
                })
                .catch(error => {
                    this.message = "Error: " + error.message;
                });
        },
        resetForm() {
            // Reinicia todos los campos del formulario después del registro exitoso
            this.sexo = '';
            this.fechaNacimiento = '';
            this.horaNacimiento = '';
            this.lugarNacimiento = '';
            this.peso = null;
            this.longitud = null;
            this.nombrePadre = '';
            this.nombreMadre = '';
            this.telefonoContacto = '';
            this.emailContacto = '';
            this.observaciones = '';
            this.tipoNacimiento = '';
            this.frecuenciaCardiaca = null;
            this.temperatura = null;
            this.presionArterialSistolica = null;
            this.presionArterialDiastolica = null;
        }
    }
}
</script>