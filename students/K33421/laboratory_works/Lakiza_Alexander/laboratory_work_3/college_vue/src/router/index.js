import Vue from 'vue'
import VueRouter from 'vue-router'
import SignUp from '../views/SignUp'
import SignIn from '../views/SignIn'
// import Home from '../views/Home.vue'
import HomeDeputy from '../views/HomeDeputy'
import HomeManager from '../views/HomeManager'
import Student from '../views/Student'
import StudentCreate from '../views/StudentCreate'
import Teacher from '../views/Teacher'
import TeacherCreate from '../views/TeacherCreate'
import TeacherEdit from '../views/TeacherEdit'
import Subject from '../views/Subject'
import SubjectCreate from '../views/SubjectCreate'
import SubjectEdit from '../views/SubjectEdit'
import Mark from '../views/Mark'
import MarkCreate from '../views/MarkCreate'
import MarkEdit from '../views/MarkEdit'
import Group from '../views/Group'
import GroupCreate from '../views/GroupCreate'
import GroupEdit from '../views/GroupEdit'
import StudentEdit from '../views/StudentEdit'
import Pair from '../views/Pair'
import PairCreate from '../views/PairCreate'
import PairEdit from '../views/PairEdit'
import GroupList from '../views/GroupList'
import GroupSchedule from '../views/GroupSchedule'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  {
    path: '/deputy',
    name: 'HomeDeputy',
    component: HomeDeputy
  },
  {
    path: '/manager',
    name: 'HomeManager',
    component: HomeManager
  },
  {
    path: '/student',
    name: 'Student',
    component: Student
  },
  {
    path: '/student/create',
    name: 'StudentCreate',
    component: StudentCreate
  },
  {
    path: '/student/:student_id',
    name: 'StudentEdit',
    component: StudentEdit
  },
  {
    path: '/teacher',
    name: 'Teacher',
    component: Teacher
  },
  {
    path: '/teacher/create',
    name: 'TeacherCreate',
    component: TeacherCreate
  },
  {
    path: '/teacher/:teacher_id',
    name: 'TeacherEdit',
    component: TeacherEdit
  },
  {
    path: '/subject',
    name: 'Subject',
    component: Subject
  },
  {
    path: '/subject/create',
    name: 'SubjectCreate',
    component: SubjectCreate
  },
  {
    path: '/subject/:subject_id',
    name: 'SubjectEdit',
    component: SubjectEdit
  },
  {
    path: '/mark',
    name: 'Mark',
    component: Mark
  },
  {
    path: '/mark/create',
    name: 'MarkCreaate',
    component: MarkCreate
  },
  {
    path: '/mark/:mark_id',
    name: 'MarkEdit',
    component: MarkEdit
  },
  {
    path: '/group',
    name: 'Group',
    component: Group
  },
  {
    path: '/group/create',
    name: 'GroupCreate',
    component: GroupCreate
  },
  {
    path: '/group/:group_id',
    name: 'GroupEdit',
    component: GroupEdit
  },
  {
    path: '/pair',
    name: 'Pair',
    component: Pair
  },
  {
    path: '/pair/create',
    name: 'PairCreate',
    component: PairCreate
  },
  {
    path: '/pair/:pair_id',
    name: 'PairEdit',
    component: PairEdit
  },
  {
    path: '/grouplist/:group_id',
    name: 'GroupList',
    component: GroupList
  },
  {
    // path: '/schedule',
    path: '/schedule/:group_id',
    name: 'GroupSchedule',
    component: GroupSchedule
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
