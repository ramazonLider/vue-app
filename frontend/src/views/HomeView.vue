<script>
import { RouterLink } from 'vue-router';
import axios from "axios";

export default {

  components: {
    RouterLink,
  },

  data() {
    return {
      products: [],
    };
  },

  mounted() {
    this.getProducts();
  },

  methods: {
    async getProducts() {
      await axios.get('/products/')
        .then(response => {
          this.products = response.data;
          console.log(response);
        })
        .catch(error => {
          console.log(error)
        })
    },
  },

}

</script>

<template>
  <main class="main" id="top">
    <!-- ============================================-->
    <!-- <section> begin ============================-->
    <section class="py-0">
      <div class="container-small">
        <div class="ecommerce-topbar">
          <nav class="navbar navbar-expand-lg navbar-light px-0">
            <div class="row gx-0 gy-2 w-100 flex-between-center">
              <div class="col-auto">
                <RouterLink class="text-decoration-none" to="../../../index.html">
                  <div class="d-flex align-items-center">
                    <img src="../../../assets/img/icons/logo.png" alt="phoenix" width="27" />
                    <p class="logo-text ms-2">phoenix</p>
                  </div>
                </RouterLink>
              </div>
              <div class="col-auto order-md-1">
                <ul class="navbar-nav navbar-nav-icons flex-row me-n2">
                  <li class="nav-item d-flex align-items-center">
                    <div class="theme-control-toggle fa-icon-wait px-2">
                      <input class="form-check-input ms-0 theme-control-toggle-input" type="checkbox"
                        data-theme-control="phoenixTheme" value="dark" id="themeControlToggle" />
                      <label class="mb-0 theme-control-toggle-label theme-control-toggle-light" for="themeControlToggle"
                        data-bs-toggle="tooltip" data-bs-placement="left" title="Switch theme">
                        <span class="icon" data-feather="moon"></span>
                      </label>
                      <label class="mb-0 theme-control-toggle-label theme-control-toggle-dark" for="themeControlToggle"
                        data-bs-toggle="tooltip" data-bs-placement="left" title="Switch theme">
                        <span class="icon" data-feather="sun"></span>
                      </label>
                    </div>
                  </li>
                  <li class="nav-item">
                    <RouterLink class="nav-link px-2 icon-indicator icon-indicator-primary"
                      to="../../../apps/e-commerce/landing/cart.html" role="button">
                      <span class="text-body-tertiary" data-feather="shopping-cart"
                        style="height:20px;width:20px;"></span>
                      <span class="icon-indicator-number">3</span>
                    </RouterLink>
                  </li>
                  <li class="nav-item dropdown">
                    <RouterLink class="nav-link px-2 icon-indicator icon-indicator-sm icon-indicator-danger"
                      id="navbarTopDropdownNotification" to="#" role="button" data-bs-toggle="dropdown"
                      data-bs-auto-close="outside" aria-haspopup="true" aria-expanded="false">
                      <span class="text-body-tertiary" data-feather="bell" style="height:20px;width:20px;"></span>
                    </RouterLink>
                    <div
                      class="dropdown-menu dropdown-menu-end notification-dropdown-menu py-0 shadow border navbar-dropdown-caret mt-2"
                      id="navbarDropdownNotfication" aria-labelledby="navbarDropdownNotfication">
                      <div class="card position-relative border-0">
                        <div class="card-header p-2">
                          <div class="d-flex justify-content-between">
                            <h5 class="text-body-emphasis mb-0">Notifications</h5>
                            <button class="btn btn-link p-0 fs-9 fw-normal" type="button">Mark all as read</button>
                          </div>
                        </div>
                        <div class="card-body p-0">
                          <div class="scrollbar-overlay" style="height: 27rem;">
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative read border-bottom">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <img class="rounded-circle" src="../../../assets/img/team/40x40/30.webp" alt="" />
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Jessie Samson</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>💬</span>
                                      Mentioned you in a comment.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10">10m</span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">10:41 AM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative unread border-bottom">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <div class="avatar-name rounded-circle">
                                      <span>J</span>
                                    </div>
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Jane Foster</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>📅</span>
                                      Created an event.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10">20m</span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">10:20 AM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative unread border-bottom">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <img class="rounded-circle avatar-placeholder"
                                      src="../../../assets/img/team/40x40/avatar.webp" alt="" />
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Jessie Samson</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>👍</span>
                                      Liked your comment.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10">1h</span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">9:30 AM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative unread border-bottom">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <img class="rounded-circle" src="../../../assets/img/team/40x40/57.webp" alt="" />
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Kiera Anderson</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>💬</span>
                                      Mentioned you in a comment.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10"></span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">9:11 AM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative unread border-bottom">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <img class="rounded-circle" src="../../../assets/img/team/40x40/59.webp" alt="" />
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Herman Carter</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>👤</span>
                                      Tagged you in a comment.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10"></span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">10:58 PM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="px-2 px-sm-3 py-3 notification-card position-relative read ">
                              <div class="d-flex align-items-center justify-content-between position-relative">
                                <div class="d-flex">
                                  <div class="avatar avatar-m status-online me-3">
                                    <img class="rounded-circle" src="../../../assets/img/team/40x40/58.webp" alt="" />
                                  </div>
                                  <div class="flex-1 me-sm-3">
                                    <h4 class="fs-9 text-body-emphasis">Benjamin Button</h4>
                                    <p class="fs-9 text-body-highlight mb-2 mb-sm-3 fw-normal">
                                      <span class='me-1 fs-10'>👍</span>
                                      Liked your comment.<span
                                        class="ms-2 text-body-quaternary text-opacity-75 fw-bold fs-10"></span>
                                    </p>
                                    <p class="text-body-secondary fs-9 mb-0">
                                      <span class="me-1 fas fa-clock"></span>
                                      <span class="fw-bold">10:18 AM </span>
                                      August 7,2021
                                    </p>
                                  </div>
                                </div>
                                <div class="d-none d-sm-block">
                                  <button
                                    class="btn fs-10 btn-sm dropdown-toggle dropdown-caret-none transition-none notification-dropdown-toggle"
                                    type="button" data-bs-toggle="dropdown" data-boundary="window" aria-haspopup="true"
                                    aria-expanded="false" data-bs-reference="parent">
                                    <span class="fas fa-ellipsis-h fs-10 text-body"></span>
                                  </button>
                                  <div class="dropdown-menu dropdown-menu-end py-2">
                                    <RouterLink class="dropdown-item" to="#!">Mark as unread</RouterLink>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="card-footer p-0 border-top border-translucent border-0">
                          <div class="my-2 text-center fw-bold fs-10 text-body-tertiary text-opactity-85">
                            <RouterLink class="fw-bolder" to="../../../pages/notifications.html">Notification history</RouterLink>
                          </div>
                        </div>
                      </div>
                    </div>
                  </li>
                  <li class="nav-item dropdown">
                    <RouterLink class="nav-link px-2" id="navbarDropdownUser" to="#" role="button" data-bs-toggle="dropdown"
                      data-bs-auto-close="outside" aria-haspopup="true" aria-expanded="false">
                      <span class="text-body-tertiary" data-feather="user" style="height:20px;width:20px;"></span>
                    </RouterLink>
                    <div
                      class="dropdown-menu dropdown-menu-end navbar-dropdown-caret py-0 dropdown-profile shadow border mt-2"
                      aria-labelledby="navbarDropdownUser">
                      <div class="card position-relative border-0">
                        <div class="card-body p-0">
                          <div class="text-center pt-4 pb-3">
                            <div class="avatar avatar-xl ">
                              <img class="rounded-circle " src="../../../assets/img/team/72x72/57.webp" alt="" />
                            </div>
                            <h6 class="mt-2 text-body-emphasis">Jerry Seinfield</h6>
                          </div>
                          <div class="mb-3 mx-3">
                            <input class="form-control form-control-sm" id="statusUpdateInput" type="text"
                              placeholder="Update your status" />
                          </div>
                        </div>
                        <div class="overflow-auto scrollbar" style="height: 10rem;">
                          <ul class="nav d-flex flex-column mb-2 pb-1">
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="user"></span>
                                <span>Profile</span>
                              </RouterLink>
                            </li>
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="pie-chart"></span>
                                Dashboard
                              </RouterLink>
                            </li>
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="lock"></span>
                                Posts &amp;Activity
                              </RouterLink>
                            </li>
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="settings"></span>
                                Settings &amp;Privacy
                              </RouterLink>
                            </li>
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="help-circle"></span>
                                Help Center
                              </RouterLink>
                            </li>
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="globe"></span>
                                Language
                              </RouterLink>
                            </li>
                          </ul>
                        </div>
                        <div class="card-footer p-0 border-top border-translucent">
                          <ul class="nav d-flex flex-column my-3">
                            <li class="nav-item">
                              <RouterLink class="nav-link px-3" to="#!">
                                <span class="me-2 text-body" data-feather="user-plus"></span>
                                Add another account
                              </RouterLink>
                            </li>
                          </ul>
                          <hr />
                          <div class="px-3">
                            <RouterLink class="btn btn-phoenix-secondary d-flex flex-center w-100" to="#!">
                              <span class="me-2" data-feather="log-out"></span>
                              Sign out
                            </RouterLink>
                          </div>
                          <div class="my-2 text-center fw-bold fs-10 text-body-quaternary">
                            <RouterLink class="text-body-quaternary me-1" to="#!">Privacy policy</RouterLink>
                            &bull;<RouterLink class="text-body-quaternary mx-1" to="#!">Terms</RouterLink>
                            &bull;<RouterLink class="text-body-quaternary ms-1" to="#!">Cookies</RouterLink>
                          </div>
                        </div>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
              <div class="col-12 col-md-6">
                <div class="search-box ecommerce-search-box w-100">
                  <form class="position-relative">
                    <input class="form-control search-input search form-control-sm" type="search" placeholder="Search"
                      aria-label="Search" />
                    <span class="fas fa-search search-box-icon"></span>
                  </form>
                </div>
              </div>
            </div>
          </nav>
        </div>
      </div>
      <!-- end of .container-->
    </section>
    <!-- <section> close ============================-->
    <!-- ============================================-->
    <nav class="ecommerce-navbar navbar-expand navbar-light bg-body-emphasis justify-content-between">
      <div class="container-small d-flex flex-between-center" data-navbar="data-navbar">
        <div class="dropdown">
          <button class="btn text-body ps-0 pe-5 text-nowrap dropdown-toggle dropdown-caret-none"
            data-category-btn="data-category-btn" data-bs-toggle="dropdown">
            <span class="fas fa-bars me-2"></span>
            Category
          </button>
          <div class="dropdown-menu border border-translucent py-0 category-dropdown-menu">
            <div class="card border-0 scrollbar" style="max-height: 657px;">
              <div class="card-body p-6 pb-3">
                <div class="row gx-7 gy-5 mb-5">
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="pocket" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Collectibles &amp;Art</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Collectibles</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Antiques</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Sports memorabilia </RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Art</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="home" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Home &amp;Gardan</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Yard, Garden &amp;Outdoor</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Crafts</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Home Improvement</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Pet Supplies</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="globe" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Sporting Goods</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Outdoor Sports</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Team Sports</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Exercise &amp;Fitness</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Golf</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="monitor" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Electronics</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Computers &amp;Tablets</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Camera &amp;Photo</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">TV, Audio &amp;Surveillance</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Cell Ohone &amp;Accessories</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="truck" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Auto Parts &amp;Accessories</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">GPS &amp;Security Devices</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Rader &amp;Laser Detectors</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Care &amp;Detailing</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Scooter Parts &amp;Accessories</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="codesandbox" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Toys &amp;Hobbies</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Radio Control</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Kids Toys</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Action Figures</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Dolls &amp;Bears</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="watch" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Fashion</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Women</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Men</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Jewelry &amp;Watches</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Shoes</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="music" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Musical Instruments &amp;Gear</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Guitar</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Pro Audio Equipment</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">String</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Stage Lighting &amp;Effects</RouterLink>
                    </div>
                  </div>
                  <div class="col-12 col-sm-6 col-md-4">
                    <div class="d-flex align-items-center mb-3">
                      <span class="text-primary me-2" data-feather="grid" style="stroke-width:3;"></span>
                      <h6 class="text-body-highlight mb-0 text-nowrap">Other Categories</h6>
                    </div>
                    <div class="ms-n2">
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Video Games &amp;Consoles</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Health &amp;Beauty</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Baby</RouterLink>
                      <RouterLink class="text-body-emphasis d-block mb-1 text-decoration-none bg-body-highlight-hover px-2 py-1 rounded-2"
                        to="#!">Business &amp;Industrial</RouterLink>
                    </div>
                  </div>
                </div>
                <div class="text-center border-top border-translucent pt-3">
                  <RouterLink class="fw-bold" to="#!">
                    See all Categories<span class="fas fa-angle-right ms-1" data-fa-transform="down-1"></span>
                  </RouterLink>
                </div>
              </div>
            </div>
          </div>
        </div>
        <ul class="navbar-nav justify-content-end align-items-center">
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link ps-0 active" to="../../../apps/e-commerce/landing/homepage.html">Home</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/landing/favourite-stores.html">My Favorites Stores</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/landing/products-filter.html">Products</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/landing/wishlist.html">Wishlist</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/landing/shipping-info.html">Shipping Info</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/admin/add-product.html">Be a vendor</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link" to="../../../apps/e-commerce/landing/order-tracking.html">Track order</RouterLink>
          </li>
          <li class="nav-item" data-nav-item="data-nav-item">
            <RouterLink class="nav-link pe-0" to="../../../apps/e-commerce/landing/checkout.html">Checkout</RouterLink>
          </li>
          <li class="nav-item dropdown" data-nav-item="data-nav-item" data-more-item="data-more-item">
            <RouterLink class="nav-link dropdown-toggle dropdown-caret-none fw-bold pe-0" to="javascript: void(0)"
              id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false" data-boundary="window"
              data-bs-reference="parent">
              More<span class="fas fa-angle-down ms-2"></span>
            </RouterLink>
            <div class="dropdown-menu dropdown-menu-end category-list" aria-labelledby="navbarDropdown"
              data-category-list="data-category-list"></div>
          </li>
        </ul>
      </div>
    </nav>
    <div class="ecommerce-homepage pt-5 mb-9">
      <!-- ============================================-->
      <!-- <section> begin ============================-->
      <section class="py-0">
        <div class="container-small">
          <div class="scrollbar">
            <div class="d-flex justify-content-between">
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2 bg-warning-subtle light">
                  <span class="fs-4 uil uil-star text-warning"></span>
                </div>
                <p class="nav-label">Deals</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-shopping-bag"></span>
                </div>
                <p class="nav-label">Grocery</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-watch-alt"></span>
                </div>
                <p class="nav-label">Fashion</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-mobile-android"></span>
                </div>
                <p class="nav-label">Mobile</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-monitor"></span>
                </div>
                <p class="nav-label">Electronics</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-estate"></span>
                </div>
                <p class="nav-label">Home</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-lamp"></span>
                </div>
                <p class="nav-label">Dining</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-gift"></span>
                </div>
                <p class="nav-label">Gifts</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-wrench"></span>
                </div>
                <p class="nav-label">Tools</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-plane-departure"></span>
                </div>
                <p class="nav-label">Travel</p>
              </RouterLink>
              <RouterLink class="icon-nav-item" to="#!">
                <div class="icon-container mb-2">
                  <span class="fs-4 uil uil-palette"></span>
                </div>
                <p class="nav-label">Others</p>
              </RouterLink>
            </div>
          </div>
        </div>
        <!-- end of .container-->
      </section>
      <!-- <section> close ============================-->
      <!-- ============================================-->
      <!-- ============================================-->
      <!-- <section> begin ============================-->
      <section class="py-0 px-xl-3">
        <div class="container px-xl-0 px-xxl-3">
          <div class="row g-3 mb-9">
            <div class="col-12">
              <div class="whooping-banner w-100 rounded-3 overflow-hidden">
                <div class="bg-holder z-n1 product-bg"
                  style="background-image:url(../../../assets/img/e-commerce/whooping_banner_product.png);background-position: bottom right;">
                </div>
                <!--/.bg-holder-->
                <div class="bg-holder z-n1 shape-bg"
                  style="background-image:url(../../../assets/img/e-commerce/whooping_banner_shape_2.png);background-position: bottom left;">
                </div>
                <!--/.bg-holder-->
                <div class="banner-text" data-bs-theme="light">
                  <h2 class="text-warning-light fw-bolder fs-lg-3 fs-xxl-2">
                    Whooping <span class="gradient-text">60% </span>
                    Off
                  </h2>
                  <h3 class="fw-bolder fs-lg-5 fs-xxl-3 text-white">on everyday items</h3>
                </div>
                <RouterLink class="btn btn-lg btn-primary rounded-pill banner-button" to="#!">Shop Now</RouterLink>
              </div>
            </div>
            <div class="col-12 col-xl-6">
              <div class="gift-items-banner w-100 rounded-3 overflow-hidden">
                <div class="bg-holder z-n1 banner-bg"
                  style="background-image:url(../../../assets/img/e-commerce/gift-items-banner-bg.png);"></div>
                <!--/.bg-holder-->
                <div class="banner-text text-md-center">
                  <h2 class="text-white fw-bolder fs-xl-4">
                    Get <span class="gradient-text">10% Off </span>
                    <br class="d-md-none">on gift items
                  </h2>
                  <RouterLink class="btn btn-lg btn-primary rounded-pill banner-button" to="#!">Buy Now</RouterLink>
                </div>
              </div>
            </div>
            <div class="col-12 col-xl-6">
              <div class="best-in-market-banner d-flex h-100 px-4 px-sm-7 py-5 px-md-11 rounded-3 overflow-hidden">
                <div class="bg-holder z-n1 banner-bg"
                  style="background-image:url(../../../assets/img/e-commerce/best-in-market-bg.png);"></div>
                <!--/.bg-holder-->
                <div class="row align-items-center w-sm-100">
                  <div class="col-8">
                    <div class="banner-text">
                      <h2 class="text-white fw-bolder fs-sm-4 mb-5">
                        MI 11 Pro<br>
                        <span class="fs-7 fs-sm-6">Best in the market</span>
                      </h2>
                      <RouterLink class="btn btn-lg btn-warning rounded-pill banner-button" to="#!">Buy Now</RouterLink>
                    </div>
                  </div>
                  <div class="col-4">
                    <img class="w-100 w-sm-75" src="../../../assets/img/e-commerce/5.png" alt="">
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="row g-4 mb-6">
            <div class="col-12 col-lg-9 col-xxl-10">
              <div class="d-flex flex-between-center mb-3">
                <div class="d-flex">
                  <span class="fas fa-bolt text-warning fs-6"></span>
                  <h3 class="mx-2">Top Deals today</h3>
                  <span class="fas fa-bolt text-warning fs-6"></span>
                </div>
                <RouterLink class="btn btn-link btn-lg p-0 d-none d-md-block" to="#!">
                  Explore more<span class="fas fa-chevron-right fs-9 ms-1"></span>
                </RouterLink>
              </div>
              <div class="swiper-theme-container products-slider">
                <div class="swiper swiper theme-slider"
                  data-swiper='{"slidesPerView":1,"spaceBetween":16,"breakpoints":{"450":{"slidesPerView":2,"spaceBetween":16},"768":{"slidesPerView":3,"spaceBetween":20},"1200":{"slidesPerView":4,"spaceBetween":16},"1540":{"slidesPerView":5,"spaceBetween":16}}}'>
                  <div class="swiper-wrapper">
                    <div v-for="product in products" :key="product.id" class="swiper-slide">
                      <div class="position-relative text-decoration-none product-card h-100">
                        <div class="d-flex flex-column justify-content-between h-100">
                          <div>
                            <div class="border border-1 border-translucent rounded-3 position-relative mb-3">
                              <button class="btn btn-wish btn-wish-primary z-2 d-toggle-container"
                                data-bs-toggle="tooltip" data-bs-placement="top" title="Add to wishlist">
                                <span class="fas fa-heart d-block-hover"></span>
                                <span class="far fa-heart d-none-hover"></span>
                              </button>
                              <img class="img-fluid" :src="product.image.url" :alt="Image" />
                            </div>
                            <RouterLink class="stretched-link" to="../../../apps/e-commerce/landing/product-details.html">
                              <h6 class="mb-2 lh-sm line-clamp-3 product-name">{{ product.name }}
                              </h6>
                            </RouterLink>
                            <p class="fs-9">
                              <span class="fa fa-star text-warning"></span>
                              <span class="fa fa-star text-warning"></span>
                              <span class="fa fa-star text-warning"></span>
                              <span class="fa fa-star text-warning"></span>
                              <span class="fa fa-star text-warning"></span>
                              <span class="text-body-quaternary fw-semibold ms-1">(67 people rated)</span>
                            </p>
                          </div>
                          <div>
                            <p class="fs-9 text-body-highlight fw-bold mb-2">{{ product.slug }}</p>
                            <div class="d-flex align-items-center mb-1">
                              <p class="me-2 text-body text-decoration-line-through mb-0">${{ product.price }}</p>
                              <h3 class="text-body-emphasis mb-0">${{ product.price  }}</h3>
                            </div>
                            <p class="text-body-tertiary fw-semibold fs-9 lh-1 mb-0">2 colors</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="swiper-nav swiper-product-nav">
                  <div class="swiper-button-next">
                    <span class="fas fa-chevron-right nav-icon"></span>
                  </div>
                  <div class="swiper-button-prev">
                    <span class="fas fa-chevron-left nav-icon"></span>
                  </div>
                </div>
              </div>
              <RouterLink class="fw-bold d-md-none px-0" to="#!">
                Explore more<span class="fas fa-chevron-right fs-9 ms-1"></span>
              </RouterLink>
            </div>
            <div class="col-lg-3 d-none d-lg-block col-xxl-2">
              <div class="h-100 position-relative rounded-3 overflow-hidden">
                <div class="bg-holder" style="background-image:url(../../../assets/img/e-commerce/4.png);"></div>
                <!--/.bg-holder-->
              </div>
            </div>
            <div class="col-12 d-lg-none">
              <RouterLink to="#!">
                <img class="w-100 rounded-3" src="../../../assets/img/e-commerce/6.png" alt="" />
              </RouterLink>
            </div>
          </div>
          <div class="row flex-center mb-15 mt-11 gy-6">
            <div class="col-auto">
              <img class="d-dark-none" src="../../../assets/img/spot-illustrations/light_30.png" alt="" width="305" />
              <img class="d-light-none" src="../../../assets/img/spot-illustrations/dark_30.png" alt="" width="305" />
            </div>
            <div class="col-auto">
              <div class="text-center text-lg-start">
                <h3 class="text-body-highlight mb-2">
                  <span class="fw-semibold">Want to have the </span>
                  ultimate <br class="d-md-none" />customer experience?
                </h3>
                <h1 class="display-3 fw-semibold mb-4">
                  Become a <span class="text-primary fw-bolder">member </span>
                  today!
                </h1>
                <RouterLink class="btn btn-lg btn-primary px-7" to="../../../pages/authentication/simple/sign-up.html">
                  Sign up<span class="fas fa-chevron-right ms-2 fs-9"></span>
                </RouterLink>
              </div>
            </div>
          </div>
        </div>
        <!-- end of .container-->
      </section>
      <!-- <section> close ============================-->
      <!-- ============================================-->
    </div>
    <!-- ============================================-->
    <!-- <section> begin ============================-->
    <section class="bg-body-highlight dark__bg-gray-1100 py-9">
      <div class="container-small">
        <div class="row justify-content-between gy-4">
          <div class="col-12 col-lg-4">
            <div class="d-flex align-items-center mb-3">
              <img src="../../../assets/img/icons/logo.png" alt="phoenix" width="27" />
              <p class="logo-text ms-2">phoenix</p>
            </div>
            <p class="text-body-tertiary mb-1 fw-semibold lh-sm fs-9">Phoenix is an admin dashboard template with
              fascinating features and amazing layout. The template is responsive to all major browsers and is compatible
              with all available devices and screen sizes.</p>
          </div>
          <div class="col-6 col-md-auto">
            <h5 class="fw-bolder mb-3">About Phoenix</h5>
            <div class="d-flex flex-column">
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Careers</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Affiliate Program</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Privacy Policy</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Terms & Conditions</RouterLink>
            </div>
          </div>
          <div class="col-6 col-md-auto">
            <h5 class="fw-bolder mb-3">Stay Connected</h5>
            <div class="d-flex flex-column">
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Blogs</RouterLink>
              <RouterLink class="mb-1 fw-semibold fs-9 d-flex" to="#!">
                <span class="fab fa-facebook-square text-primary me-2 fs-8"></span>
                <span class="text-body-secondary">Facebook</span>
              </RouterLink>
              <RouterLink class="mb-1 fw-semibold fs-9 d-flex" to="#!">
                <span class="fab fa-twitter-square text-info me-2 fs-8"></span>
                <span class="text-body-secondary">Twitter</span>
              </RouterLink>
            </div>
          </div>
          <div class="col-6 col-md-auto">
            <h5 class="fw-bolder mb-3">Customer Service</h5>
            <div class="d-flex flex-column">
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Help Desk</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Support, 24/7</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Community of Phoenix</RouterLink>
            </div>
          </div>
          <div class="col-6 col-md-auto">
            <h5 class="fw-bolder mb-3">Payment Method</h5>
            <div class="d-flex flex-column">
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Cash on Delivery</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Online Payment</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">PayPal</RouterLink>
              <RouterLink class="text-body-tertiary fw-semibold fs-9 mb-1" to="#!">Installment</RouterLink>
            </div>
          </div>
        </div>
      </div>
      <!-- end of .container-->
    </section>
    <!-- <section> close ============================-->
    <!-- ============================================-->
    <footer class="footer position-relative">
      <div class="row g-0 justify-content-between align-items-center h-100">
        <div class="col-12 col-sm-auto text-center">
          <p class="mb-0 mt-2 mt-sm-0 text-body">
            Thank you for creating with Phoenix<span class="d-none d-sm-inline-block"></span>
            <span class="d-none d-sm-inline-block mx-1">|</span>
            <br class="d-sm-none" />
            2024 &copy;<RouterLink class="mx-1" to="https://themewagon.com">Themewagon</RouterLink>
          </p>
        </div>
        <div class="col-12 col-sm-auto text-center">
          <p class="mb-0 text-body-tertiary text-opacity-85">v1.16.0</p>
        </div>
      </div>
    </footer>
  </main>
  <div class="offcanvas offcanvas-end settings-panel border-0" id="settings-offcanvas" tabindex="-1"
    aria-labelledby="settings-offcanvas">
    <div class="offcanvas-header align-items-start border-bottom flex-column border-translucent">
      <div class="pt-1 w-100 mb-6 d-flex justify-content-between align-items-start">
        <div>
          <h5 class="mb-2 me-2 lh-sm">
            <span class="fas fa-palette me-2 fs-8"></span>
            Theme Customizer
          </h5>
          <p class="mb-0 fs-9">Explore different styles according to your preferences</p>
        </div>
        <button class="btn p-1 fw-bolder" type="button" data-bs-dismiss="offcanvas" aria-label="Close">
          <span class="fas fa-times fs-8"></span>
        </button>
      </div>
      <button class="btn btn-phoenix-secondary w-100" data-theme-control="reset">
        <span class="fas fa-arrows-rotate me-2 fs-10"></span>
        Reset to default
      </button>
    </div>
    <div class="offcanvas-body scrollbar px-card" id="themeController">
      <div class="setting-panel-item mt-0">
        <h5 class="setting-panel-item-title">Color Scheme</h5>
        <div class="row gx-2">
          <div class="col-4">
            <input class="btn-check" id="themeSwitcherLight" name="theme-color" type="radio" value="light"
              data-theme-control="phoenixTheme" />
            <label class="btn d-inline-block btn-navbar-style fs-9" for="themeSwitcherLight">
              <span class="mb-2 rounded d-block">
                <img class="img-fluid img-prototype mb-0" src="../../../assets/img/generic/default-light.png" alt="" />
              </span>
              <span class="label-text">Light</span>
            </label>
          </div>
          <div class="col-4">
            <input class="btn-check" id="themeSwitcherDark" name="theme-color" type="radio" value="dark"
              data-theme-control="phoenixTheme" />
            <label class="btn d-inline-block btn-navbar-style fs-9" for="themeSwitcherDark">
              <span class="mb-2 rounded d-block">
                <img class="img-fluid img-prototype mb-0" src="../../../assets/img/generic/default-dark.png" alt="" />
              </span>
              <span class="label-text">Dark</span>
            </label>
          </div>
          <div class="col-4">
            <input class="btn-check" id="themeSwitcherAuto" name="theme-color" type="radio" value="auto"
              data-theme-control="phoenixTheme" />
            <label class="btn d-inline-block btn-navbar-style fs-9" for="themeSwitcherAuto">
              <span class="mb-2 rounded d-block">
                <img class="img-fluid img-prototype mb-0" src="../../../assets/img/generic/auto.png" alt="" />
              </span>
              <span class="label-text">Auto</span>
            </label>
          </div>
        </div>
      </div>
      <div class="border border-translucent rounded-3 p-4 setting-panel-item bg-body-emphasis">
        <div class="d-flex justify-content-between align-items-center">
          <h5 class="setting-panel-item-title mb-1">RTL </h5>
          <div class="form-check form-switch mb-0">
            <input class="form-check-input ms-auto" type="checkbox" data-theme-control="phoenixIsRTL" />
          </div>
        </div>
        <p class="mb-0 text-body-tertiary">Change text direction</p>
      </div>
      <div class="border border-translucent rounded-3 p-4 setting-panel-item bg-body-emphasis">
        <div class="d-flex justify-content-between align-items-center">
          <h5 class="setting-panel-item-title mb-1">Support Chat </h5>
          <div class="form-check form-switch mb-0">
            <input class="form-check-input ms-auto" type="checkbox" data-theme-control="phoenixSupportChat" />
          </div>
        </div>
        <p class="mb-0 text-body-tertiary">Toggle support chat</p>
      </div>
      <div class="setting-panel-item">
        <h5 class="setting-panel-item-title">Navigation Type</h5>
        <div class="row gx-2">
          <div class="col-6">
            <input class="btn-check" id="navbarPositionVertical" name="navigation-type" type="radio" value="vertical"
              data-theme-control="phoenixNavbarPosition" disabled="disabled" />
            <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarPositionVertical">
              <span class="mb-2 rounded d-block">
                <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/default-light.png"
                  alt="" />
                <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/default-dark.png"
                  alt="" />
              </span>
              <span class="label-text">Vertical</span>
            </label>
          </div>
          <div class="col-6">
            <input class="btn-check" id="navbarPositionHorizontal" name="navigation-type" type="radio" value="horizontal"
              data-theme-control="phoenixNavbarPosition" disabled="disabled" />
            <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarPositionHorizontal">
              <span class="mb-2 rounded d-block">
                <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/top-default.png"
                  alt="" />
                <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/top-default-dark.png"
                  alt="" />
              </span>
              <span class="label-text">Horizontal</span>
            </label>
          </div>
        </div>
        <div class="col-6">
          <input class="btn-check" id="navbarPositionCombo" name="navigation-type" type="radio" value="combo"
            data-theme-control="phoenixNavbarPosition" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarPositionCombo">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/nav-combo-light.png"
                alt="" />
              <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/nav-combo-dark.png"
                alt="" />
            </span>
            <span class="label-text">Combo</span>
          </label>
        </div>
        <div class="col-6">
          <input class="btn-check" id="navbarPositionTopDouble" name="navigation-type" type="radio" value="dual-nav"
            data-theme-control="phoenixNavbarPosition" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarPositionTopDouble">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/dual-light.png"
                alt="" />
              <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/dual-dark.png"
                alt="" />
            </span>
            <span class="label-text">Dual nav</span>
          </label>
        </div>
      </div>
      <p class="text-warning-dark font-medium">
        <span class="fa-solid fa-triangle-exclamation me-2 text-warning"></span>
        You can't update navigation type in this page
      </p>
    </div>
    <div class="setting-panel-item">
      <h5 class="setting-panel-item-title">Vertical Navbar Appearance</h5>
      <div class="row gx-2">
        <div class="col-6">
          <input class="btn-check" id="navbar-style-default" type="radio" name="config.name" value="default"
            data-theme-control="phoenixNavbarVerticalStyle" disabled="disabled" />
          <label class="btn d-block w-100 btn-navbar-style fs-9" for="navbar-style-default">
            <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/default-light.png"
              alt="" />
            <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/default-dark.png"
              alt="" />
            <span class="label-text d-dark-none">Default</span>
            <span class="label-text d-light-none">Default</span>
          </label>
        </div>
        <div class="col-6">
          <input class="btn-check" id="navbar-style-dark" type="radio" name="config.name" value="darker"
            data-theme-control="phoenixNavbarVerticalStyle" disabled="disabled" />
          <label class="btn d-block w-100 btn-navbar-style fs-9" for="navbar-style-dark">
            <img class="img-fluid img-prototype d-dark-none" src="../../../assets/img/generic/vertical-darker.png"
              alt="" />
            <img class="img-fluid img-prototype d-light-none" src="../../../assets/img/generic/vertical-lighter.png"
              alt="" />
            <span class="label-text d-dark-none">Darker</span>
            <span class="label-text d-light-none">Lighter</span>
          </label>
        </div>
      </div>
      <p class="text-warning-dark font-medium">
        <span class="fa-solid fa-triangle-exclamation me-2 text-warning"></span>
        You can't update vertical navbar appearance in this page
      </p>
    </div>
    <div class="setting-panel-item">
      <h5 class="setting-panel-item-title">Horizontal Navbar Shape</h5>
      <div class="row gx-2">
        <div class="col-6">
          <input class="btn-check" id="navbarShapeDefault" name="navbar-shape" type="radio" value="default"
            data-theme-control="phoenixNavbarTopShape" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarShapeDefault">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none mb-0" src="../../../assets/img/generic/top-default.png"
                alt="" />
              <img class="img-fluid img-prototype d-light-none mb-0"
                src="../../../assets/img/generic/top-default-dark.png" alt="" />
            </span>
            <span class="label-text">Default</span>
          </label>
        </div>
        <div class="col-6">
          <input class="btn-check" id="navbarShapeSlim" name="navbar-shape" type="radio" value="slim"
            data-theme-control="phoenixNavbarTopShape" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarShapeSlim">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none mb-0" src="../../../assets/img/generic/top-slim.png"
                alt="" />
              <img class="img-fluid img-prototype d-light-none mb-0" src="../../../assets/img/generic/top-slim-dark.png"
                alt="" />
            </span>
            <span class="label-text">Slim</span>
          </label>
        </div>
      </div>
      <p class="text-warning-dark font-medium">
        <span class="fa-solid fa-triangle-exclamation me-2 text-warning"></span>
        You can't update horizontal navbar shape in this page
      </p>
    </div>
    <div class="setting-panel-item">
      <h5 class="setting-panel-item-title">Horizontal Navbar Appearance</h5>
      <div class="row gx-2">
        <div class="col-6">
          <input class="btn-check" id="navbarTopDefault" name="navbar-top-style" type="radio" value="default"
            data-theme-control="phoenixNavbarTopStyle" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarTopDefault">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none mb-0" src="../../../assets/img/generic/top-default.png"
                alt="" />
              <img class="img-fluid img-prototype d-light-none mb-0"
                src="../../../assets/img/generic/top-style-darker.png" alt="" />
            </span>
            <span class="label-text">Default</span>
          </label>
        </div>
        <div class="col-6">
          <input class="btn-check" id="navbarTopDarker" name="navbar-top-style" type="radio" value="darker"
            data-theme-control="phoenixNavbarTopStyle" disabled="disabled" />
          <label class="btn d-inline-block btn-navbar-style fs-9" for="navbarTopDarker">
            <span class="mb-2 rounded d-block">
              <img class="img-fluid img-prototype d-dark-none mb-0"
                src="../../../assets/img/generic/navbar-top-style-light.png" alt="" />
              <img class="img-fluid img-prototype d-light-none mb-0"
                src="../../../assets/img/generic/top-style-lighter.png" alt="" />
            </span>
            <span class="label-text d-dark-none">Darker</span>
            <span class="label-text d-light-none">Lighter</span>
          </label>
        </div>
      </div>
      <p class="text-warning-dark font-medium">
        <span class="fa-solid fa-triangle-exclamation me-2 text-warning"></span>
        You can't update horizontal navbar appearance in this page
      </p>
    </div>
    <RouterLink class="bun btn-primary d-grid mb-3 text-white mt-5 btn btn-primary"
      to="https://themes.getbootstrap.com/product/phoenix-admin-dashboard-webapp-template/" target="_blank">Purchase
      template</RouterLink>
  </div>
  <RouterLink class="card setting-toggle" to="#settings-offcanvas" data-bs-toggle="offcanvas">
    <div class="card-body d-flex align-items-center px-2 py-1">
      <div class="position-relative rounded-start" style="height:34px;width:28px">
        <div class="settings-popover">
          <span class="ripple">
            <span class="fa-spin position-absolute all-0 d-flex flex-center">
              <span class="icon-spin position-absolute all-0 d-flex flex-center">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="#ffffff" xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M19.7369 12.3941L19.1989 12.1065C18.4459 11.7041 18.0843 10.8487 18.0843 9.99495C18.0843 9.14118 18.4459 8.28582 19.1989 7.88336L19.7369 7.59581C19.9474 7.47484 20.0316 7.23291 19.9474 7.03131C19.4842 5.57973 18.6843 4.28943 17.6738 3.20075C17.5053 3.03946 17.2527 2.99914 17.0422 3.12011L16.393 3.46714C15.6883 3.84379 14.8377 3.74529 14.1476 3.3427C14.0988 3.31422 14.0496 3.28621 14.0002 3.25868C13.2568 2.84453 12.7055 2.10629 12.7055 1.25525V0.70081C12.7055 0.499202 12.5371 0.297594 12.2845 0.257272C10.7266 -0.105622 9.16879 -0.0653007 7.69516 0.257272C7.44254 0.297594 7.31623 0.499202 7.31623 0.70081V1.23474C7.31623 2.09575 6.74999 2.8362 5.99824 3.25599C5.95774 3.27861 5.91747 3.30159 5.87744 3.32493C5.15643 3.74527 4.26453 3.85902 3.53534 3.45302L2.93743 3.12011C2.72691 2.99914 2.47429 3.03946 2.30587 3.20075C1.29538 4.28943 0.495411 5.57973 0.0322686 7.03131C-0.051939 7.23291 0.0322686 7.47484 0.242788 7.59581L0.784376 7.8853C1.54166 8.29007 1.92694 9.13627 1.92694 9.99495C1.92694 10.8536 1.54166 11.6998 0.784375 12.1046L0.242788 12.3941C0.0322686 12.515 -0.051939 12.757 0.0322686 12.9586C0.495411 14.4102 1.29538 15.7005 2.30587 16.7891C2.47429 16.9504 2.72691 16.9907 2.93743 16.8698L3.58669 16.5227C4.29133 16.1461 5.14131 16.2457 5.8331 16.6455C5.88713 16.6767 5.94159 16.7074 5.99648 16.7375C6.75162 17.1511 7.31623 17.8941 7.31623 18.7552V19.2891C7.31623 19.4425 7.41373 19.5959 7.55309 19.696C7.64066 19.7589 7.74815 19.7843 7.85406 19.8046C9.35884 20.0925 10.8609 20.0456 12.2845 19.7729C12.5371 19.6923 12.7055 19.4907 12.7055 19.2891V18.7346C12.7055 17.8836 13.2568 17.1454 14.0002 16.7312C14.0496 16.7037 14.0988 16.6757 14.1476 16.6472C14.8377 16.2446 15.6883 16.1461 16.393 16.5227L17.0422 16.8698C17.2527 16.9907 17.5053 16.9504 17.6738 16.7891C18.7264 15.7005 19.4842 14.4102 19.9895 12.9586C20.0316 12.757 19.9474 12.515 19.7369 12.3941ZM10.0109 13.2005C8.1162 13.2005 6.64257 11.7893 6.64257 9.97478C6.64257 8.20063 8.1162 6.74905 10.0109 6.74905C11.8634 6.74905 13.3792 8.20063 13.3792 9.97478C13.3792 11.7893 11.8634 13.2005 10.0109 13.2005Z"
                    fill="#2A7BE4"></path>
                </svg>
              </span>
            </span>
          </span>
        </div>
      </div>
      <small class="text-uppercase text-body-tertiary fw-bold py-2 pe-2 ps-1 rounded-end">customize</small>
    </div>
  </RouterLink>

</template>
