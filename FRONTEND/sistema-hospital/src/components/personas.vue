<template>
    <h1 class="text-3xl mb-4">Datos personales</h1>


    <form class="grid grid-cols-3 gap-4 p">
        <div>
        <label class="block mb-2 text-indigo-500" for="username">Nombre</label>
        <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
            type="text" name="username"></div>

        <div>
            <label class="block mb-2 text-indigo-500" for="username">Apellido Paterno</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="text" name="username">
        </div>

        <div>
            <label class="block mb-2 text-indigo-500" for="username">Apellido Materno</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="text" name="username">
        </div>
        <div>
            <label class="block mb-2 text-indigo-500" for="username">CURP</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="text" name="username">
        </div>

        <div>
            <label class="block mb-2 text-indigo-500" for="username">Genero</label>
            <select id="countries"
                class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300">
                <option selected>Seleccionar</option>
                <option value="H">Hombre</option>
                <option value="M">Mujer</option>
                <option value="Otro">Otro</option>
            </select>
        </div>

        <div>
            <label class="block mb-2 text-indigo-500" for="username">Sangre</label>
            <select id="countries"
                class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300">
                <option selected>Seleccionar</option>
                <option value="O+">O+</option>
                <option value="O-">O-</option>
                <option value="A+">A+</option>
                <option value="A-">A-</option>
            </select>
        </div>



        <div>
            <label class="block mb-2 text-indigo-500" for="password">Fecha de Nacimiento</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="date" name="password">
        </div>
        <div>
            <label class="block mb-2 text-indigo-500" for="password">Telefono</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="number" name="password">
        </div>

        <div>
            <label class="block mb-2 text-indigo-500" for="password">Correo</label>
            <input class="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300"
                type="email" name="password">
        </div>
    </form>

</template>