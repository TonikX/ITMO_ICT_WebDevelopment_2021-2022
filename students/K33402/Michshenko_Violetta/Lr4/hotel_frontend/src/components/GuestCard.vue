<template>
    <div>
        <v-card v-if="edit" class="elevation-4">
            <v-toolbar color="primary" dark>
                <v-toolbar-title>Edit Form</v-toolbar-title>
            </v-toolbar>
            <v-card-text>
                <v-form>
                    <v-text-field required v-model="name" name="Имя" label="Имя" type="text"></v-text-field>
                    <v-text-field required v-model="surname" name="Фамилия" label="Фамилия" type="text"></v-text-field>
                    <v-text-field required v-model="middlename" name="Отчество" label="Отчество" type="text"></v-text-field>
                    <v-text-field required v-model="passport_number" name="Пасспорт" label="Пасспорт" type="text"></v-text-field>
                    <v-text-field required v-model="from_location" name="Страна" label="Страна" type="text"></v-text-field>
                    <v-text-field required v-model="check_in_date" name="Дата Заселения" label="Дата Заселения" type="text"></v-text-field>
                    <v-text-field required v-model="room" name="Номер Комнаты" label="Номер Комнаты" type="text"></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" dark @click="edit=false">Close</v-btn>
                <v-btn color="primary" dark @click="editGuest">Submit Edit</v-btn>
            </v-card-actions>
        </v-card>

        <v-card v-if="del" class="elevation-4">
            <v-card-title>Are you sure?</v-card-title>
            <v-card-actions>
                <v-btn color="primary" dark @click="del=false">Close</v-btn>
                <v-btn color="primary" dark @click="deleteGuest">Yeah. Delete.</v-btn>
            </v-card-actions>
        </v-card>

        <v-card v-if="exist" elevation="6" shaped>
            <v-card-title>{{ guest.name }} {{guest.middlename}} {{guest.surname}}</v-card-title>
            <v-card-subtitle>{{ guest.passport_number }}</v-card-subtitle>
            <v-card-text>Дата заселения:{{ guest.check_in_date }} Комната: {{ guest.room }}</v-card-text>
            <v-car-actions>

                <v-btn @click="edit = true">Edit</v-btn>
                <v-btn @click="del = true">Delete</v-btn>
            </v-car-actions>
        </v-card>
    </div>
</template>

<script>
export default {
  name: "GuestCard",
  props: {
    guest: Object,
  },
  data: () => ({
    exist: true,
    edit: false,
    del: false,
    passport_number: null,
    name: null,
    surname: null,
    middlename: null,
    from_location: null,
    check_in_date: null,
    room: null,
  }),

  methods: {
    editGuest() {
      const body = {
        passport_number: this.passport_number,
        name: this.name,
        surname: this.surname,
        middlename: this.middlename,
        from_location: this.from_location,
        check_in_date: this.check_in_date,
        room: this.room,
      };

      this.axios
        .patch(this.$hostname + "hotel/guests/" + this.guest.id + "/", body, {
          headers: {
            Authorization: "Token " + localStorage.getItem("auth_token"),
          },
        })
        .then(response => {
          console.log(response);
          this.guest.passport_number = this.passport_number;
          this.guest.name = this.name;
          this.guest.surname = this.surname;
          this.guest.middlename = this.middlename;
          this.guest.from_location = this.from_location;
          this.guest.check_in_date = this.check_in_date;
          this.guest.room = this.room;
          this.edit = false;
        })
        .catch(error => console.log(error));

      //Уже 5 часов ночи я не буду эмитить события в guests
    },

    deleteGuest() {
      this.axios
        .delete(this.$hostname + "hotel/guests/" + this.guest.id + "/", {
          headers: { Authorization: "Token " + localStorage.getItem("auth_token") },
        })
        .then(response => {
          console.log(response);
          this.exist = false;
          this.del = false;
        })
        .catch(error => console.log(error));
    },
  },
};
</script>
