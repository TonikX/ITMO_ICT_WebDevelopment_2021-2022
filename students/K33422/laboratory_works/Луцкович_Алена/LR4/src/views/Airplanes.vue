<template>
  <v-data-table
      :headers="headers"
      :items="planes"
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
              Add plane
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
                        v-model="editedItem.type"
                        label="Тип"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.tail_number"
                        label="Номер самолета"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.seats"
                        label="Число мест"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.velocity"
                        label="Крейсерская скорость"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.airline"
                        label="Авиакомпания"
                    ></v-text-field>
                  </v-col>
                  <v-col
                      cols="12"
                      sm="6"
                      md="4"
                  >
                    <v-text-field
                        v-model="editedItem.under_maintenance"
                        label="В ремонте"
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
        text: 'Номер самолета',
        align: 'start',
        sortable: false,
        value: 'tail_number'
      },
      { text: 'Тип', value: 'type' },
      { text: 'Число мест', value: 'seats' },
      { text: 'Крейсерская скорость', value: 'velocity' },
      { text: 'Авиакомпания', value: 'airline' },
      { text: 'В ремонте', value: 'under_maintenance'},
      { text: 'Редактирование', value: 'actions', sortable: false }
    ],
    planes: [],
    editedIndex: -1,
    editedItem: {
      tail_number: '',
      type: '',
      seats: '',
      velocity: '',
      airline: '',
      under_maintenance: ''
    },
    defaultItem: {
      tail_number: '',
      type: '',
      seats: '',
      velocity: '',
      airline: '',
      under_maintenance: ''
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New airplane' : 'Edit airplane'
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
    this.PlaneList()
  },
  methods: {
    async PlaneList () {
      try {
        const response = await axios
            .get('http://127.0.0.1:8000/airplanes/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.planes = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.planes.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.planes.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.planes.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/airplanes/' + JSON.stringify(this.editedItem.id), {
          tail_number: this.editedItem.tail_number,
          type: this.editedItem.type,
          seats: this.editedItem.seats,
          velocity: this.editedItem.velocity,
          airline: this.editedItem.airline,
          under_maintenance: this.editedItem.under_maintenance
        })
      } else {
        this.planes.push(this.editedItem)
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
    async createPlane () {
      try {
        const response = await this.axios
            .post('http://localhost:8000/airplanes/create/', {
              tail_number: this.editedItem.tail_number,
              type: this.editedItem.type,
              seats: this.editedItem.seats,
              velocity: this.editedItem.velocity,
              airline: this.editedItem.airline,
              under_maintenance: this.editedItem.under_maintenance
            })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updatePlane () {
      this.editedIndex = 1
      try {
        const response = await this.axios
            .put('http://localhost:8000/airplanes/' + JSON.stringify(this.editedItem.id) + '/', {
              tail_number: this.editedItem.tail_number,
              type: this.editedItem.type,
              seats: this.editedItem.seats,
              velocity: this.editedItem.velocity,
              airline: this.editedItem.airline,
              under_maintenance: this.editedItem.under_maintenance
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
        this.updatePlane()
      } else {
        this.createPlane()
      }
    }
  }
}
</script>
<style scoped>
</style>
