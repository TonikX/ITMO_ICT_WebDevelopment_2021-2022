<template>
  <v-data-table
    :headers="headers"
    :items="tranzity"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Транзиты</v-toolbar-title>
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
              color="lime darken-2"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              Добавить транзит
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
                      v-model="editedItem.punkt_peresadki"
                      label="Пункт пересадки"
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
            <v-card-title class="headline">Вы уверены, что хотите удалить этот транзит?</v-card-title>
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
        text: 'ID Транзита',
        align: 'start',
        sortable: false,
        value: 'id'
      },
      { text: 'Пункт пересадки', value: 'punkt_peresadki' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    tranzity: [],
    editedIndex: -1,
    editedItem: {
      punkt_peresadki: ''
    },
    defaultItem: {
      punkt_peresadki: ''
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'Новый транзит' : 'Редактировать транзит'
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
    this.TranzitList()
  },
  methods: {
    async TranzitList () {
      try {
        const response = await axios
          .get('http://127.0.0.1:8000/api/tranzit/')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.tranzity = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.tranzity.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.tranzity.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.tranzity.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/api/tranzit/' + JSON.stringify(this.editedItem.id), {
          punkt_peresadki: this.editedItem.punkt_peresadki
        })
      } else {
        this.tranzity.push(this.editedItem)
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
    async createTranzit () {
      try {
        const response = await this.axios
          .post('http://localhost:8000/api/tranzit/create/', {
            punkt_peresadki: this.editedItem.punkt_peresadki
          })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('API ERROR', e)
      }
    },
    async updateTranzit () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://localhost:8000/api/tranzit/' + JSON.stringify(this.editedItem.id) + '/', {
            punkt_peresadki: this.editedItem.punkt_peresadki
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
        this.updateTranzit()
      } else {
        this.createTranzit()
      }
    }
  }
}
</script>
<style scoped>
</style>
