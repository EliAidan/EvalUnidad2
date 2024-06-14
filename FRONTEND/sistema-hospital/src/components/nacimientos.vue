<template>
    <div class="bg-gray-900 text-white p-8 rounded-lg">
        <h2 class="text-2xl font-bold mb-4">Registro de Bebé</h2>

        <div v-if="message" class="mb-4">
            {{ message }}
        </div>

        <form @submit.prevent="submitForm" class="grid grid-cols-1 md:grid-cols-2 gap-4">
            
            

           

            <div class="md:col-span-2">
                <button type="submit" class="w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-md">Registrar Bebé</button>
            </div>
        </form>
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