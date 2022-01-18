<template>
  <div>
    <div>
      <v-btn @click='$router.go(-1)' elevation="4">Back</v-btn>&nbsp;&nbsp;
      <v-btn @click='$router.push("/deputy")' elevation="4">Home</v-btn>
      <h2 style="margin-top: 20px;">Schedule</h2>
      <span style="font-size:1.3vw"><strong>Group: {{ cur_gr_name }}</strong></span>
      <p></p>
    </div>
    <h3>Monday</h3>
    <template v-if="MonPairs.length === 0">
      <p>There are no pairs on Monday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in MonPairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Tuesday</h3>
    <template v-if="TuePairs.length === 0">
      <p>There are no pairs on Tuesday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in TuePairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Wednesday</h3>
    <template v-if="WedPairs.length === 0">
      <p>There are no pairs on Wednesday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in WedPairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Thursday</h3>
    <template v-if="ThuPairs.length === 0">
      <p>There are no pairs on Thursday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in ThuPairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Friday</h3>
    <template v-if="FriPairs.length === 0">
      <p>There are no pairs on Friday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in FriPairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Saturday</h3>
    <template v-if="SatPairs.length === 0">
      <p>There are no pairs on Saturday! Chill!</p>
    </template>
    <template v-else>
      <table>
        <tr>
          <td><strong>Pair number</strong></td>
          <td><strong>Subject</strong></td>
          <td><strong>Room</strong></td>
          <td><strong>Teacher</strong></td>
        </tr>
        <tr v-for="pair in SatPairs" :key="pair.id">
          <td>{{ pair.pair_number }}</td>
          <td>{{ pair.subject }}</td>
          <td>{{ pair.room }}</td>
          <td>{{ pair.teacher }}</td>
        </tr>
      </table>
    </template>
    <v-divider></v-divider>
    <h3>Sunday is always a day off! Extra chill!</h3>
  </div>
</template>

<script>
export default {
  name: 'GroupSchedule',
  data: () => ({
    gr_id: 0,
    cur_gr_name: '',
    pairs: [],
    MonPairs: [],
    TuePairs: [],
    WedPairs: [],
    ThuPairs: [],
    FriPairs: [],
    SatPairs: [],
    elems: [],
    teachers: [],
    subjects: []
  }),
  async created () {
    this.gr_id = this.$route.params.group_id
    console.log(this.gr_id)
    await this.axios
      .get(`http://127.0.0.1:8000/group/${this.gr_id}`)
      .then((res) => {
        console.log(res.data)
        this.cur_gr_name = res.data.name
      })
    await this.axios
      .get('http://127.0.0.1:8000/pair/list/')
      .then((res) => {
        this.pairs = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/group/list/')
      .then((res) => {
        console.log('this.groups', res.data)
        this.groups = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/teacher/list/')
      .then((res) => {
        console.log('this.teachers', res.data)
        this.teachers = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    await this.axios
      .get('http://127.0.0.1:8000/subject/list')
      .then((res) => {
        console.log('this.subjects', res.data)
        this.subjects = res.data
      })
      .catch((error) => {
        console.log(error)
      })
    console.log('this.pairs.length', this.pairs)
    for (const i of this.pairs) {
      if (i.group.toString() === this.gr_id.toString()) {
        console.log('i', i)
        const gro = this.groups.filter(val => val.id === i.group)[0]
        const tea = this.teachers.filter(val => val.id === i.teacher)[0]
        const sub = this.subjects.filter(val => val.id === i.subject)[0]
        this.elems.push({
          id: i.id,
          pair_number: i.pair_number,
          name_day: i.name_day,
          room: i.room,
          group: gro.name,
          subject: sub.name,
          teacher: `${tea.first_name} ${tea.last_name}`
        })
      }
    }
    console.log(this.elems.length)
    for (const para of this.elems) {
      if (para.name_day === 'Mon') {
        this.MonPairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      } else if (para.name_day === 'Tue') {
        this.TuePairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      } else if (para.name_day === 'Wed') {
        this.WedPairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      } else if (para.name_day === 'Thu') {
        this.ThuPairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      } else if (para.name_day === 'Fri') {
        this.FriPairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      } else if (para.name_day === 'Sat') {
        this.SatPairs.push({
          id: para.id,
          pair_number: para.pair_number,
          room: para.room,
          subject: para.subject,
          teacher: para.teacher
        })
      }
    }
    this.MonPairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
    this.TuePairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
    this.WedPairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
    this.ThuPairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
    this.FriPairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
    this.SatPairs.sort(function (a, b) {
      return a.pair_number - b.pair_number
    })
  }
}
</script>

<style>
table {
  margin-top: 10px;
  width: 100%;
}

td {
  text-align: left;
  padding: 0.5rem;
}

.v-divider {
  margin-bottom: 10px;
}
</style>
