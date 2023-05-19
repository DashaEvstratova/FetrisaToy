<template>
  <!-- Footer -->
  <MDBFooter :text="['center', 'lg-start', 'muted']">
    <!-- Section: Social media -->
    <section
      class="d-flex justify-content-center justify-content-lg-between p-4 border-bottom"
    >
      <div class="me-5 d-none d-lg-block">
        <span>Get connected with us on social networks:</span>
      </div>
      <div>
        <a href="https://www.google.com/" class="me-4 text-reset">
          <MDBIcon
            class="link-secondary"
            iconStyle="fab"
            icon="google"
          ></MDBIcon>
        </a>
          <a href="https://www.instagram.com/fetrisa_toy/" class="me-4 text-reset">
              <MDBIcon
                      class="link-secondary"
            iconStyle="fab"
            icon="instagram"
          ></MDBIcon>
        </a>
        <a href="https://vk.com/fetrisa_toy" class="me-4 text-reset">
          <MDBIcon
            class="link-secondary"
            iconStyle="fab"
            icon="vk"
          ></MDBIcon>
        </a>
      </div>
      <!-- Right -->
    </section>
    <!-- Section: Social media -->

    <!-- Section: Links  -->
    <section class="">
      <MDBContainer class="text-center text-md-start mt-5">
        <!-- Grid row -->
        <MDBRow class="mt-3">
          <MDBCol md="2" lg="2" xl="2" class="mx-auto mb-4">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4">Покупателям</h6>
            <p>
              <a href="/delivery" class="text-reset">Доставка</a>
            </p>
            <p>
              <a href="/payinfo" class="text-reset">Способ оплаты</a>
            </p>
            <p>
              <a href="/questions_and_answers" class="text-reset">Вопросы и ответы</a>
            </p>
          </MDBCol>
          <MDBCol md="3" lg="2" xl="2" class="mx-auto mb-4">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4">Компания</h6>
            <p>
              <a href="#!" class="text-reset">О нас</a>
            </p>
            <p>
              <a href="#!" class="text-reset">Реквизиты</a>
            </p>
            <p>
              <a href="#!" class="text-reset">Контакты</a>
            </p>
          </MDBCol>
          <MDBCol md="5" lg="3" xl="3" class="mx-auto mb-md-0 mb-5">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4">Информация</h6>
            <p>
              <i class="fas fa-home me-3 link-secondary"></i> г. Казань,
                ул. Космонавтов
            </p>
            <p>
              <i class="fas fa-envelope me-3 link-secondary"></i>
              fetrisa_toy@gmail.com
            </p>
            <p>
              <MDBIcon icon="phone" class="me-3 link-secondary" />
              +7 934 234 57 88
            </p>
            <p>
              <MDBIcon icon="print" class="me-3 link-secondary" />
              +7 901 234 67 89
            </p>
          </MDBCol>
          <!-- Grid column -->
        </MDBRow>
        <!-- Grid row -->
      </MDBContainer>
    </section>
    <!-- Section: Links  -->

    <!-- Copyright -->
    <div
      class="text-center p-4"
      style="background-color: rgba(0, 0, 0, 0.05)"
    >
      © 2023:
      <a class="text-reset fw-bold" href="https://vk.com/fetrisa_toy"
        >fetrisa_toy.com</a
      >
    </div>
    <!-- Copyright -->
  </MDBFooter>
  <!-- Footer -->
</template>

<script>
  import { MDBFooter, MDBIcon, MDBRow, MDBCol, MDBContainer } from "mdb-vue-ui-kit";

  export default {
    components: {
      MDBFooter,
      MDBIcon,
      MDBRow,
      MDBCol,
      MDBContainer
    }
  }
</script>


<style scoped>

</style>