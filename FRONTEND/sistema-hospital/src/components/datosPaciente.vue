<template>
    <div>
                <label for="sexo" class="block mb-2">Sexo:</label>
                <select id="sexo" v-model="sexo" required class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
                    <option value="">Seleccionar</option>
                    <option value="Masculino">Masculino</option>
                    <option value="Femenino">Femenino</option>
                </select>
            </div>

            <div>
                <label for="fechaNacimiento" class="block mb-2">Fecha de Nacimiento:</label>
                <input type="date" id="fechaNacimiento" v-model="fechaNacimiento" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="horaNacimiento" class="block mb-2">Hora de Nacimiento:</label>
                <input type="time" id="horaNacimiento" v-model="horaNacimiento" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="lugarNacimiento" class="block mb-2">Lugar de Nacimiento:</label>
                <select id="lugarNacimiento" v-model="lugarNacimiento" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
                    <option value="">Seleccionar</option>
                    <option value="Xicotepec">Xicotepec</option>
                    <option value="Huachinango">Huachinango</option>
                    <option value="Ceiba">Villa Avila Camacho</option>
                    <option value="Necaxa">Necaxa</option>
                </select>
            </div>

            <div>
                <label for="peso" class="block mb-2">Peso (kg):</label>
                <input type="number" id="peso" v-model="peso" step="0.01" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
            </div>

            <div>
                <label for="longitud" class="block mb-2">Longitud (cm):</label>
                <input type="number" id="longitud" v-model="longitud" step="0.01" class="w-full rounded-md py-2 px-3 bg-gray-800 text-white">
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