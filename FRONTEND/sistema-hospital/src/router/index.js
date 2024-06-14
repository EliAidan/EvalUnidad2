import { createRouter, createWebHistory } from 'vue-router'
//import HomeView from '../views/HomeView.vue'
import LoginView from '../components/login.vue'
import RegisterView from '../components/registerUser.vue'
import SideBar from '../components/sidebar.vue'
import Personas from '../components/personas.vue'
// import Usuarios from '../components/usuarios.vue'
import Nacimientos from '../components/nacimientos.vue'
import Seguimiento from '../components/Seguimiento.vue'
import ListaVacunas from '../components/listaVacunas.vue'
import Vacunas from '../components/vacunas.vue'
import Medicos from '../components/datosMedicos.vue'
import Infante from '../components/datosPaciente.vue'
import Contacto from '../components/datosContacto.vue'
import PiePagina from '../components/piePagina.vue'





const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginView
    },
    {
      path: '/login',
      name: 'login',
      
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      
      component: RegisterView
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: SideBar,
      children:[
        {path:'/personas', name:'personas', component:Personas}
        ,{path:'/nacimientos',name:'nacimientos', component:Nacimientos}
        ,{path:'/seguimiento',name:'seguimiento', component:Seguimiento}
        ,{path:'/vacunas',name:'vacunas', component:Vacunas}
        ,{path:'/listaVacunas',name:'listaVacunas', component:ListaVacunas}
        ,{path:'/datosContacto',name:'contacto', component: Contacto}
        ,{path:'/datosPaciente',name:'infante', component: Infante}
        ,{path:'/datosMedicos',name:'Medicos', component: Medicos}
        ,{path:'/piePagina',name:'PiePagina', component: PiePagina}   
      ]
      
    }
  ]
})

export default router
