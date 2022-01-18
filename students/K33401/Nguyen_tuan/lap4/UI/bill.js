const bill={template:`
<div>

<button type="button" style="width: 300px"
class="btn btn-primary m-2 fload-end"
data-bs-toggle="modal"
data-bs-target="#exampleModal"
@click="addClick()">
 Add Bill
</button>
<table class="table table-striped">
<thead>
    <tr>
        <th>
            Bill_id
        </th>
        <th>
            Check_in
        </th>
        <th>
            Check_out
        </th>
        <th>
            Hotel_name
        </th>
        <th>
            Adress_hotel
        </th>
        <th>
            Money
        </th>
        <th>
            Options
        </th>
    </tr>
</thead>
<tbody>
    <tr v-for="dep in bill">
        <td>{{dep.bill_id}}</td>
        <td>{{dep.check_in}}</td>
        <td>{{dep.check_out}}</td>
        <td>{{dep.hotel_name}}</td>
        <td>{{dep.adress_hotel}}</td>
        <td>{{dep.money}}</td>
        <td>
            <button type="button"
            class="btn btn-light mr-1"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
            @click="editClick(dep)">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16">
                <path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/>
                </svg>
            </button> 
            <button type="button" @click="deleteClick(dep.bill_id)" class="btn btn-light mr1">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z"/>
                </svg>
            </button>
        </td>
    </tr>
</tbody>
</table>
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelleddy="exampleModaLabel" aria-hidden="true">
<div class="modal-dialog modal-lg modal-dialog-centered">
<div class="modal-content">
    <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">{{modalTitle}}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
    </div>

    <div class="modal-body" >
        <div class="input-group mb-3">
            <span class="input-group-text" style="width: 120px"> Check_in </span>
            <input type="date" class="form-control" v-model="check_in">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" style="width: 120px"> Check_out </span>
            <input type="date" class="form-control" v-model="check_out">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" style="width: 120px"> Hotel_name </span>
            <input type="text" class="form-control" v-model="hotel_name">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" style="width: 120px"> Adress_hotel </span>
            <input type="text" class="form-control" v-model="adress_hotel">
        </div>
        <div class="input-group mb-3">
            <span class="input-group-text" style="width: 120px"> Money </span>
            <input type="interger" class="form-control" v-model="money">
        </div>
        <button type="button" @click="createClick()"
        v-if="bill_id==0" class="btn btn-primary">
        Create
        </button>
    
        <button type="button" @click="updateClick()"
        v-if="bill_id!=0" class="btn btn-primary">
        Update
        </button>
    </div>
</div>
</div>
</div>

</div>


`,

data(){
    return{
        bill:[],
        modalTitle:"",
        check_in:"",
        check_out:"",
        hotel_name:"",
        adress_hotel:"",
        money:0,
        bill_id:0,
    }
},
methods:{
    refreshData(){
        axios.get(variables.API_URL+"bill")
        .then((response)=>{
            this.bill=response.data;
        });
    },
    addClick(){
        this.modalTitle="Add Bill";
        this.bill_id=0;
        this.check_in="";
        this.check_out="";
        this.hotel_name="";
        this.adress_hotel="";
        this.money=0;
    },
    editClick(bill){
        this.modalTitle="Edit Bill";
        this.bill_id=bill.bill_id;
        this.check_in=bill.check_in;
        this.check_out=bill.check_out;
        this.hotel_name=bill.hotel_name;
        this.adress_hotel=bill.adress_hotel;
        this.money=bill.money;
    },
    createClick(){
        axios.post(variables.API_URL+"bill",{
            check_in:this.check_in,
            check_out:this.check_out,
            hotel_name:this.hotel_name,
            adress_hotel:this.adress_hotel,
            money:this.money
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    },
    updateClick(){
        axios.put(variables.API_URL+"bill",{
            bill_id:this.bill_id,
            check_in:this.check_in,
            check_out:this.check_out,
            hotel_name:this.hotel_name,
            adress_hotel:this.adress_hotel,
            money:this.money,
        })
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    },
    deleteClick(id){
        if(!confirm("Are you sure?")){
            return;
        }
        axios.delete(variables.API_URL+"bill/"+id)
        .then((response)=>{
            this.refreshData();
            alert(response.data);
        });
    }
},
mounted:function(){
    this.refreshData();
}
}