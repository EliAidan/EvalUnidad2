<template>
    <div>
                <label for="nombrePadre" class="block mb-2">Nombre del Padre:</label>
                <input type="text" id="nombrePadre" v-model="nombrePadre" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="nombreMadre" class="block mb-2">Nombre de la Madre:</label>
                <input type="text" id="nombreMadre" v-model="nombreMadre" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="telefonoContacto" class="block mb-2">Teléfono de Contacto:</label>
                <input type="text" id="telefonoContacto" v-model="telefonoContacto" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="emailContacto" class="block mb-2">Email de Contacto:</label>
                <input type="email" id="emailContacto" v-model="emailContacto" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
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