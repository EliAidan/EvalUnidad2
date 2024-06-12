<template>


   <button data-drawer-target="sidebar-multi-level-sidebar" data-drawer-toggle="sidebar-multi-level-sidebar"
      aria-controls="sidebar-multi-level-sidebar" type="button"
      class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-green-200 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
      <span class="sr-only">Open sidebar</span>
      <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
         xmlns="http://www.w3.org/2000/svg">
         <path clip-rule="evenodd" fill-rule="evenodd"
            d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z">
         </path>
      </svg>
   </button>

   <aside id="sidebar-multi-level-sidebar"
      class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
      aria-label="Sidebar">
      <div class="h-full px-3 py-4 overflow-y-auto" style="background-color: #d3e3fd ">
         <ul class="space-y-2 font-medium">
            <li>
               <a href="#"
                  class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-green-200 dark:hover:bg-gray-700 group">
                  <span class="material-symbols-outlined">Home</span>
                  <span class="ms-3">Dashboard</span>
               </a>
            </li>

            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example00" data-collapse-toggle="dropdown-example00">
                  <span class="material-symbols-outlined"><span
                        class="material-symbols-outlined">folder_managed</span></span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Direccion General</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example00" class="hidden py-2 space-y-2">
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Aprobación
                        de servicio</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Estructura
                        organica</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Datos
                        estadisticos</a>
                  </li>

                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Bitacora</a>
                  </li>
               </ul>
            </li>
            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example0" data-collapse-toggle="dropdown-example0">
                  <span class="material-symbols-outlined">diversity_3</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Recursos Humanos</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>

               <ul id="dropdown-example0" class="hidden py-2 space-y-2">
                  
                        <li>
                           <RouterLink to="/personas">
                              <a href="#"
                                 class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Personas</a>
                           </RouterLink>
                        </li>
                     


                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Puestos</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Personal
                        Médico</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Horarios</a>
                  </li>
               </ul>

            </li>






            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example1" data-collapse-toggle="dropdown-example1">
                  <span class="material-symbols-outlined">surgical</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Programación<br>Quirúrgica</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example1" class="hidden py-2 space-y-2">
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Cirugías</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Calendario
                        de cirugía</a>
                  </li>

               </ul>
            </li>

            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example2" data-collapse-toggle="dropdown-example2">
                  <span class="material-symbols-outlined">radiology</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Estudios</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example2" class="hidden py-2 space-y-2">

                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Resultados
                        estudios</a>
                  </li>

                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Estudios</a>
                  </li>



               </ul>
            </li>


            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example3" data-collapse-toggle="dropdown-example3">
                  <span class="material-symbols-outlined">child_care</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Pediatria</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example3" class="hidden py-2 space-y-2">
                  <li>
                           <RouterLink to="/nacimientos">
                              <a href="#"
                                 class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Nacimientos</a>
                           </RouterLink>
                        </li>
                  <li>
                     <RouterLink to="/seguimiento">
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Desarrollo
                        Infantil</a>
                     </RouterLink>
                  </li>



               </ul>
            </li>


            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example4" data-collapse-toggle="dropdown-example4">
                  <span class="material-symbols-outlined">medication</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Farmacia</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example4" class="hidden py-2 space-y-2">
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Consumibles</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Medicamento</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Dispensación</a>
                  </li>



               </ul>
            </li>



            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example5" data-collapse-toggle="dropdown-example5">
                  <span class="material-symbols-outlined">volunteer_activism</span>
                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Transplantes</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example5" class="hidden py-2 space-y-2">
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Organos</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Solicitudes</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray  -100 dark:text-white dark:hover:bg-gray-700">Detalle
                        de organos</a>
                  </li>



               </ul>
            </li>

            <li>
               <button type="button"
                  class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700"
                  aria-controls="dropdown-example" data-collapse-toggle="dropdown-example">
                  <span class="material-symbols-outlined">how_to_reg</span>

                  <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">Registros Médicos</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none"
                     viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                        d="m1 1 4 4 4-4" />
                  </svg>
               </button>
               <ul id="dropdown-example" class="hidden py-2 space-y-2">
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Citas</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Expediente
                        médico</a>
                  </li>
                  <li>
                     <a href="#"
                        class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-green-200 dark:text-white dark:hover:bg-gray-700">Recetas
                        médicas</a>
                  </li>




               </ul>
            </li>


            <li>
               <RouterLink to="/login">
                  <a href="#"
                     class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-green-200 dark:hover:bg-gray-700 group">
                     <span class="material-symbols-outlined">logout</span>
                     <span class="flex-1 ms-3 whitespace-nowrap">Cerrar sesión</span>
                  </a>
               </RouterLink>
            </li>

            
               

         </ul>
      </div>



   
      
   </aside>




   <div class="p-4 sm:ml-64">
      <router-view />
      <PiePagina></PiePagina>
      <!-- 
   <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
      <div class="grid grid-cols-3 gap-4 mb-4">
         <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center h-24 rounded bg-gray-50 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
      </div>
      <div class="flex items-center justify-center h-48 mb-4 rounded bg-gray-50 dark:bg-gray-800">
         <p class="text-2xl text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
               <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
            </svg>
         </p>
      </div>
      <div class="grid grid-cols-2 gap-4 mb-4">
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
      </div>
      <div class="flex items-center justify-center h-48 mb-4 rounded bg-gray-50 dark:bg-gray-800">
         <p class="text-2xl text-gray-400 dark:text-gray-500">
            <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
               <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
            </svg>
         </p>
      </div>
      <div class="grid grid-cols-2 gap-4">
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
         <div class="flex items-center justify-center rounded bg-gray-50 h-28 dark:bg-gray-800">
            <p class="text-2xl text-gray-400 dark:text-gray-500">
               <svg class="w-3.5 h-3.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 18 18">
                  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 1v16M1 9h16"/>
               </svg>
            </p>
         </div>
      </div>
   </div> -->
   </div>
   
</template>

<script>
import PiePagina from '../components/piePagina.vue'

export default {
   components: {  // Corrección en la palabra "components"
      PiePagina
   }
}
</script>
<!-- <style>
.PiePagina{
   position:fixed;
   bottom: 0;
   left: 0;
   width: 100%;
   background-color: rgb(0, 0, 0);
   z-index: 999;

}</style> -->
