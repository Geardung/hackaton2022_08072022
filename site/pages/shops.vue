<template>
  <div>
    <Title>{{ this.idx }}</Title>
    <div class="main-items">
      <div
        v-if="isError"
        style="
          display: flex;
          flex-direction: column;
          text-align: center;
          align-items: center;
          justify-content: center;
          margin-top: 10px;
        "
      >
        <img width="250px" src="/img/icons/empty-cart.svg" alt="" />
        <p style="font-weight: bold; font-size: 23px">
          Простите, но мы ничего не нашли в этом магазине
        </p>
      </div>
      <div v-else v-for="(i, id) in response">
        <div class="item">
          <img width="35px" src="/img/icons/purchase.svg" alt="" />
          <div style="text-align: right">
            <p>{{ i.cost }} ₽</p>
            <p>
              {{ i.name }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Title from "../components/Title.vue";
export default {
  data() {
    return {
      response: {},
      idx: "",
      id: "",
      isError: false,
    };
  },
  async mounted() {
    console.log(this.$route.fullPath);
    let rout = this.$route.fullPath;
    this.idx = rout.slice(8);
    console.log(this.idx);
    try {
      let result = await axios.get(
        `http://5.23.55.230:8080/get_goods_by_shop?name=${this.idx}`
      );
      let copy = { ...result.data.result };
      this.response = JSON.parse(JSON.stringify(copy));
      console.log(this.response);
    } catch (error) {
      console.log(error);
      this.isError = true;
    }
  },
  components: { Title },
};
</script>

<style scoped>
.main-items {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
.item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  border-radius: 10px;
  background: white;
  padding: 8px;
  box-shadow: 0px 1px 4px rgb(0 0 0 / 25%);
}
</style>
