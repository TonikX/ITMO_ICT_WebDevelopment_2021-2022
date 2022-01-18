<template>
  <v-data-table
      :headers="headers"
      :items="flights"
      class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
          flat
      >
        <v-spacer></v-spacer>
        <v-dialog
            v-model="dialog"
            max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
                color="orange darken-2"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
            >
              Add flight
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>

            <v-card-text>
              <v-container>
                <v-row>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.number"
                        label="Номер рейса"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.distance"
                        label="Расстояние"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.departure"
                        label="Пункт вылета"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.arrival"
                        label="Пункт назначения"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.transit"
                        label="Транзит"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.completed"
                        label="Завершенных рейсов"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                  color="red darken-1"
                  text
                  @click="close"
              >
                Cancel
              </v-btn>
              <v-btn
                  color="green darken-4"
                  text
                  @click="save"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Please confirm your intention.</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="orange darken-1" text @click="closeDelete">Cancel</v-btn>
              <v-btn color="red darken-1" text @click="deleteItemConfirm">Delete</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
          small
          @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
import axios from 'axios'
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: 'Номер рейса',
        align: 'start',
        sortable: false,
        value: 'number'
      },
      { text: 'Расстояние до пункта назначения (в км)', value: 'distance' },
      { text: 'Пункт вылета', value: 'departure' },
      { text: 'Пункт назначения', value: 'arrival' },
      { text: 'Транзит', value: 'transit' },
      { text: 'Завершенных рейсов', value: 'completed' },
      { text: 'Редактирование', value: 'actions', sortable: false }
    ],
    flights: [],
    editedIndex: -1,
    editedItem: {
      distance: '',
      departure: '',
      arrival: '',
      transit: '',
      completed: ''
    },
    defaultItem: {
      distance: '',
      departure: '',
      arrival: '',
      transit: '',
      completed: ''
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New flight' : 'Edit flight'
    }
  },
  watch: {
    dialog (val) {
      val || this.close()
    },
    dialogDelete (val) {
      val || this.closeDelete()
    }
  },
  created () {
    this.FlightList()
  },
  methods: {
    async FlightList () {
      try {
        const response = await axios
            .get('http://127.0.0.1:8000/schedule/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.flights = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.flights.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.flights.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.flights.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/schedule/' + JSON.stringify(this.editedItem.number), {
          number: this.editedItem.number,
          distance: this.editedItem.distance,
          departure: this.editedItem.departure,
          arrival: this.editedItem.arrival,
          transit: this.editedItem.transit,
          completed: this.editedItem.completed
        })
      } else {
        this.flights.push(this.editedItem)
      }
      this.close()
    },
    close () {
      this.dialog = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    closeDelete () {
      this.dialogDelete = false
      this.$nextTick(() => {
        this.editedItem = Object.assign({}, this.defaultItem)
        this.editedIndex = -1
      })
    },
    async createFlight () {
      try {
        const response = await this.axios
            .post('http://localhost:8000/schedule/create/', {
              number: this.editedItem.number,
              distance: this.editedItem.distance,
              departure: this.editedItem.departure,
              arrival: this.editedItem.arrival,
              transit: this.editedItem.transit,
              completed: this.editedItem.completed
            })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateFlight () {
      this.editedIndex = 1
      try {
        const response = await this.axios
            .put('http://localhost:8000/schedule/' + JSON.stringify(this.editedItem.number) + '/', {
              number: this.editedItem.number,
              distance: this.editedItem.distance,
              departure: this.editedItem.departure,
              arrival: this.editedItem.arrival,
              transit: this.editedItem.transit,
              completed: this.editedItem.completed
            })
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    save () {
      if (this.editedIndex > -1) {
        this.updateFlight()
      } else {
        this.createFlight()
      }
    }
  }
}
</script>
<style scoped>
</style>
