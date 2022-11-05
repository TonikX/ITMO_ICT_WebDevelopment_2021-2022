<template>
  <v-data-table
    :headers="headers"
    :items="cages"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-toolbar
        flat
      >
        <v-toolbar-title>Cages</v-toolbar-title>
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
              color="primary"
              dark
              class="mb-2"
              v-bind="attrs"
              v-on="on"
            >
              ADD
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
                      v-model="editedItem.cage"
                      label="Cage"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.row"
                      label="Row"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.shed"
                      label="Shed"
                    ></v-text-field>
                  </v-col>
                  <v-col
                    cols="12"
                    sm="6"
                    md="4"
                  >
                    <v-text-field
                      v-model="editedItem.square"
                      label="Square"
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
                Cancel
              </v-btn>
              <v-btn
                color="blue darken-4"
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
            <v-card-title class="headline">Are you sure?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="deleteItemConfirm">Yes</v-btn>
              <v-btn color="blue darken-1" text @click="closeDelete">No</v-btn>
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
    flag: false,
    headers: [
      { text: 'Cage', value: 'cage' },
      { text: 'Row', value: 'row' },
      { text: 'Shed', value: 'shed' },
      { text: 'Square', value: 'square' },
      { text: 'Actions', value: 'actions', sortable: false }
    ],
    cages: [],
    editedIndex: -1,
    editedItem: {
      cage: 0,
      row: 0,
      shed: 0,
      square: 0
    },
    defaultItem: {
      cage: 0,
      row: 0,
      shed: 0,
      square: 0
    }
  }),
  computed: {
    formTitle () {
      return this.editedIndex === -1 ? 'New Item' : 'Edit Item'
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
    this.cagesList()
  },
  methods: {
    async cagesList () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/cage/list')
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.cages = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    editItem (item) {
      this.editedIndex = this.cages.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    deleteItem (item) {
      this.editedIndex = this.cages.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
    },
    deleteItemConfirm () {
      if (this.editedIndex > -1) {
        this.cages.splice(this.editedIndex, 1)
        this.closeDelete()
        axios.delete('http://127.0.0.1:8000/cage/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          cage: this.editedItem.cage,
          row: this.editedItem.row,
          shed: this.editedItem.shed,
          square: this.editedItem.square
        })
      } else {
        this.cages.push(this.editedItem)
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
    save () {
      if (this.editedIndex > -1) {
        Object.assign(this.cages[this.editedIndex], this.editedItem)
        axios.put('http://127.0.0.1:8000/cage/info/' + JSON.stringify(this.editedItem.id), {
          id: this.editedItem.id,
          cage: this.editedItem.cage,
          row: this.editedItem.row,
          shed: this.editedItem.shed,
          square: this.editedItem.square
        })
          .then(response => {
            console.log(response)
            // ans = response.status
          })
      } else {
        console.log('posting new data . . .')
        // ans = error.status
        axios.post('http://127.0.0.1:8000/cage/create/', {
          cage: this.editedItem.cage,
          row: this.editedItem.row,
          shed: this.editedItem.shed,
          square: this.editedItem.square
        })
      }
      this.close()
    }
  }
}
</script>
