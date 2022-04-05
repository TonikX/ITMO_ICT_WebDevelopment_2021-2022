<template>
  <v-data-table
    :headers="headers"
    :items="ekipazhi"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Экипажи</v-toolbar-title>
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
              color="red"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Добавить экипаж
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
                      v-model="editedItem.name"
                      label="Ekipazh"
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
                color="gray darken-1"
                text
                @click="close"
              >
                Отмена
              </v-btn>
              <v-btn
                color="gray darken-4"
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
            <v-card-title class="headline">Вы уверены, что хотите удалить этот экипаж?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="gray darken-1" text @click="closeDelete">Назад</v-btn>
              <v-btn color="gray darken-1" text @click="deleteItemConfirm">Удалить</v-btn>
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
        text: 'Экипаж',
        align: 'start',
        sortable: false,
        value: 'name'
      },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    ekipazhi: [],
    editedIndex: -1,
    editedItem: {
      name: ''
    },
    defaultItem: {
      name: ''
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Новый экипаж' : 'Редактировать экипаж'
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
    this.ekipazhList()
  },
  methods: {
    async ekipazhList () {
      try {
        const response = await axios
          .get('http://127.0.0.1:8000/api/ekipazh/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.ekipazhi = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.ekipazhi.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.ekipazhi.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.ekipazhi.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/api/ekipazh/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          name: this.editedItem.name
        })
      } else {
        this.ekipazhi.push(this.editedItem)
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
    async createEkipazh () {
      try {
        const response = await this.axios
          .post('http://localhost:8000/api/ekipazh/create/', {
            name: this.editedItem.name
          })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateEkipazh () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://localhost:8000/api/ekipazh/' + JSON.stringify(this.editedItem.id) + '/', {
            id: this.editedItem.id,
            name: this.editedItem.name
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
        this.updateEkipazh()
      } else {
        this.createEkipazh()
      }
    }
  }
}
</script>
<style scoped>
</style>
