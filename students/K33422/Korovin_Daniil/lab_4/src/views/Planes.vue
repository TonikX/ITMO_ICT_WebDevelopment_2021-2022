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
        <v-toolbar-title>Самолёты</v-toolbar-title>
        <v-divider
          class="mx-4"
          inset
          vertical
        ></v-divider>
        <v-spacer></v-spacer>
        <v-dialog
          v-model="dialog"
          max-width="500px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="pink darken-2"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Добавить самолёт
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
                  </v-col>
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
                      v-model="editedItem.number"
                      label="Номер модели"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.mesta"
                      label="Количество мест"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.speed"
                      label="Крейсерская скорость"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.avia"
                      label="Авиакомпания"
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
                color="blue darken-1"
                text
                @click="close"
              >
                Отмена
              </v-btn>
              <v-btn
                color="blue darken-4"
                text
                @click="save"
              >
                Сохранить
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Вы точно уверены, что хотите удалить самолёт?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Назад</v-btn>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">Удалить</v-btn>
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
        text: 'Тип',
        align: 'start',
        sortable: false,
        value: 'type'
      },
      { text: 'Номер модели', value: 'number' },
      { text: 'Количество мест', value: 'mesta' },
      { text: 'Крейсерская скорость', value: 'speed' },
      { text: 'Авиакомпания', value: 'avia' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    planes: [],
    editedIndex: -1,
    editedItem: {
      mesta: '',
      speed: '',
      avia: ''
    },
    defaultItem: {
      type: '',
      number: '',
      mesta: '',
      speed: '',
      avia: ''
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Новый самолёт' : 'Редактировать самолёт'
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
          .get('http://127.0.0.1:8000/api/planes/')
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
        axios.delete('http://127.0.0.1:8000/api/plane/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          number: this.editedItem.number,
          distance: this.editedItem.distance,
          punkt_start: this.editedItem.punkt_start,
          punkt_end: this.editedItem.punkt_end,
          id_tranzita: this.editedItem.id_tranzita
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
          .post('http://localhost:8000/api/plane/create/', {
            type: this.editedItem.type,
            number: this.editedItem.number,
            mesta: this.editedItem.mesta,
            speed: this.editedItem.speed,
            avia: this.editedItem.avia
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
          .put('http://localhost:8000/api/plane/' + JSON.stringify(this.editedItem.id) + '/', {
            type: this.editedItem.type,
            number: this.editedItem.number,
            mesta: this.editedItem.mesta,
            speed: this.editedItem.speed,
            avia: this.editedItem.avia
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
