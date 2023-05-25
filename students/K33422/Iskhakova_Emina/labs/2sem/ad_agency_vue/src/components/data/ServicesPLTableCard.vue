<template>
   <v-data-table
     :headers="headers"
     :items="services"
     sort-by="id"
     item-key="title"
     dark
   >
     <template v-for="(col, i) in filters" v-slot:[`header.${i}`]="{ header }">
       <v-menu :close-on-content-click="false"
               :nudge-width="200"
               fixed
               left
               offset-y
               style="position: absolute; right: 0"
               transition="slide-y-transition"
               v-bind:key="col"
               dark
       >
         <template v-slot:activator="{ on, attrs }">
           <v-btn color="indigo" icon v-bind="attrs" v-on="on">
             <v-icon small>
               mdi-filter-variant
             </v-icon>
           </v-btn>
         </template>
         <v-list flat dense class="pa-0">
           <v-list-item-group multiple v-model="activeFilters[header.value]" class="py-2">
             <template v-for="(item, ) in filters[header.value]">
               <v-list-item :key="`${item}`" :value="item" :ripple="false">
                 <template v-slot:default="{ active, toggle }">
                   <v-list-item-action>
                     <v-checkbox :input-value="active" :true-value="item"
                                 @click="toggle" color="primary" :ripple="false" dense></v-checkbox>
                   </v-list-item-action>
                   <v-list-item-content>
                     <v-list-item-title v-text="item"></v-list-item-title>
                   </v-list-item-content>
                 </template>
               </v-list-item>
             </template>
           </v-list-item-group>
           <v-divider></v-divider>
           <v-row no-gutters>
             <v-col cols="6">
               <v-btn text block @click="toggleAll(header.value)" color="success">Выделить все</v-btn>
             </v-col>
             <v-col cols="6">
               <v-btn text block @click="clearAll(header.value)" color="warning">Очистить все</v-btn>
             </v-col>
           </v-row>
         </v-list>
       </v-menu>
     </template>
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title>Прайс-лист на услуги</v-toolbar-title>
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-dialog v-model="dialog" max-width="500px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn color="primary" dark class="mb-2" v-bind="attrs" v-on="on">Добавить новую услугу</v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">{{ formTitle }}</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-row>
                    <v-col cols="12" sm="6" md="4">
                      <v-select
                      v-model="editedItem.service_type"
                      :items=service_types
                      item-text="name"
                      item-value="abbr"
                      label="Service type"
                    ></v-select>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.title" label="Title"></v-text-field>
                    </v-col>
                    <v-col cols="12" sm="6" md="4">
                      <v-text-field v-model="editedItem.price" label="Price"></v-text-field>
                    </v-col>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="close">Отмена</v-btn>
                <v-btn color="blue darken-1" text @click="save">Сохранить</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-dialog v-model="dialogDelete" max-width="500px">
          <v-card>
            <v-card-title class="headline">Вы уверены, что хотите удалить эту услугу?</v-card-title>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="closeDelete">Отмена</v-btn>
              <v-btn color="blue darken-1" text @click="DeleteService">Подтвердить</v-btn>
              <v-spacer></v-spacer>
            </v-card-actions>
          </v-card>
        </v-dialog>
        </v-toolbar>
      </template>
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click="deleteItem(item)">
          mdi-delete
        </v-icon>
      </template>
    </v-data-table>
</template>

<script>
export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    filters: { service_type: [] },
    activeFilters: {},
    services: [],
    service_types: [
      { name: 'печатная реклама', abbr: 'п' },
      { name: 'реклама в интерьере внутри помещения', abbr: 'и' },
      { name: 'реклама на транспортных средствах', abbr: 'т' },
      { name: 'уличная реклама', abbr: 'у' }
    ],
    editedIndex: -1,
    editedItem: {
      service_type: 'у',
      title: '',
      price: 0
    },
    defaultItem: {
      service_type: 'у',
      title: '',
      price: 0
    }
  }),

  computed: {
    headers () {
      return [
        { text: 'id', value: 'id' },
        {
          text: 'service_type',
          value: 'service_type',
          filter: value => {
            return this.activeFilters.service_type ? this.activeFilters.service_type.includes(value) : true
          }
        },
        { text: 'title', value: 'title' },
        { text: 'price', value: 'price' },
        { text: 'Actions', value: 'actions', sortable: false }
      ]
    },
    formTitle () {
      return this.editedIndex === -1 ? 'Добавить услугу' : 'Изменение данных об услуге'
    }
  },

  watch: {
    dialog (val) {
      val || this.close()
    },
    services (val) {
      this.initFilters()
    }
  },

  created () {
    this.GetServices()
  },

  methods: {
    async GetServices () {
      try {
        const response = await this.axios
          .get('http://127.0.0.1:8000/ad_agency/servicespl/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        this.services = response.data
        return response.data
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async CreateService () {
      try {
        const response = await this.axios
          .post('http://127.0.0.1:8000/ad_agency/servicespl/create/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })
        if (response.status !== 201) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async UpdateService () {
      this.editedIndex = 1
      try {
        const response = await this.axios
          .put('http://127.0.0.1:8000/ad_agency/servicespl/' + this.editedItem.id + '/', this.editedItem, { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })
        if (response.status !== 200) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },
    async DeleteService () {
      this.editedIndex = 1
      this.dialogDelete = true
      try {
        const response = await this.axios
          .delete('http://127.0.0.1:8000/ad_agency/servicespl/' + this.editedItem.id + '/', { headers: { Authorization: 'Token ' + localStorage.getItem('token') } })
        if (response.status !== 204) {
          throw new Error(response.status)
        }
        window.location.reload()
      } catch (e) {
        console.error('AN API ERROR', e)
      }
    },

    initFilters () {
      for (const col in this.filters) {
        this.filters[col] = this.services.map((d) => { return d[col] }).filter(
          (value, index, self) => { return self.indexOf(value) === index }
        )
      }
      this.activeFilters = Object.assign({}, this.filters)
    },

    toggleAll (col) {
      this.activeFilters[col] = this.services.map((d) => { return d[col] }).filter(
        (value, index, self) => { return self.indexOf(value) === index }
      )
    },

    clearAll (col) {
      this.activeFilters[col] = []
    },

    editItem (item) {
      this.editedIndex = this.services.indexOf(item)
      this.editedItem = Object.assign({}, item)
      this.editedItem.service_type = this.service_types.find(item => item.name === this.editedItem.service_type).abbr
      this.dialog = true
    },

    deleteItem (item) {
      this.editedIndex = 1
      this.editedItem = Object.assign({}, item)
      this.dialogDelete = true
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
        this.UpdateService()
      } else {
        this.CreateService()
      }
      this.close()
    }
  }
}
</script>
