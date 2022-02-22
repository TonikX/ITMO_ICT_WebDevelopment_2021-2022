<template>
  <v-main>
    <v-container fluid fill-height>
      <v-layout justify-center>
        <v-flex xs12 sm8 md4>
        <template>
          <v-row justify="center">
            <v-dialog v-model="dialog" persistent max-width="600px">
              <template v-slot:activator="{ on, attrs }">
                <v-btn color="primary" dark v-bind="attrs" v-on="on">
                  Add Room
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">Add Room</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field v-model="roomNumber" label="Номер комнаты" required></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field v-model="roomPrice" label="Цена комнаты" required></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field v-model="roomFloor" label="Этаж" required></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field v-model="roomType" label="Количество кроватей" required></v-text-field>
                      </v-col>
                    </v-row>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="green darken-1" text @click="dialog = false">
                    Close Dialog
                  </v-btn>
                  <v-btn color="green darken-1" text @click="addRoom">
                    Add Room
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-row>
        </template>
        <room-card v-for="room in rooms" v-bind:key="room.number" v-bind:room="room" style="margin-top: 20px"></room-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
import RoomCard from "@/components/RoomCard.vue";

export default {
  name: "Rooms",

  components: {
    RoomCard,
  },

  data: () => ({
    rooms: [],
    filter: false,
    dialog: false,
    roomNumber: null,
    roomType: null,
    roomPrice: null,
    roomFloor: null,
  }),
  methods: {
    addRoom() {
      const body = {
        number: this.roomNumber,
        type: this.roomType,
        price: this.roomPrice,
        floor: this.roomFloor,
      };

      this.axios
        .post(this.$hostname + "hotel/rooms/", body, {
          headers: {
            Authorization: "Token " + localStorage.getItem("auth_token"),
          },
        })
        .then(response => {
          if (response.status === 201) {
            this.rooms.push(body);
          }
        })
        .catch(error => console.log(error));

      this.dialog = false;
    },
  },
  created() {
    this.axios
      .get(this.$hostname + "hotel/rooms/", {
        headers: { Authorization: "Token " + localStorage.getItem("auth_token") },
      })
      .then(response => {
        this.rooms = response.data;
      })
      .catch(error => {
        console.log(error);
      });
  },
};
</script>

<style></style>
