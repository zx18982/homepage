<template>
  <div v-if="siteLinksCategories.length > 0" class="links">
    <div class="line">
      <Icon size="20">
        <Link />
      </Icon>
      <span class="title">网站列表</span>
    </div>

    <!-- 分类 Tabs -->
    <div class="category-tabs">
      <div
        v-for="category in siteLinksCategories"
        :key="category.id"
        :class="['tab-item', { active: currentCategory === category.id }]"
        @click="switchCategory(category.id)"
      >
        {{ category.name }}
      </div>
    </div>

    <!-- 网站列表 -->
    <Swiper
      v-if="currentLinks.length > 0"
      :modules="[Pagination, Mousewheel]"
      :slides-per-view="1"
      :space-between="40"
      :pagination="{
        el: '.swiper-pagination',
        clickable: true,
        bulletElement: 'div',
      }"
      :mousewheel="true"
    >
      <SwiperSlide v-for="page in currentLinksList" :key="page">
        <div v-for="(row, rowIndex) in page" :key="rowIndex" class="link-row">
          <el-row class="link-all" :gutter="20">
            <el-col v-for="(item, index) in row" :span="8" :key="item">
              <div class="item cards" @click="jumpLink(item)">
                <img v-if="item.icon" :src="item.icon" :alt="item.name" class="site-icon" />
                <span class="name text-hidden">{{ item.name }}</span>
              </div>
            </el-col>
          </el-row>
        </div>
      </SwiperSlide>
      <div class="swiper-pagination" />
    </Swiper>
  </div>
</template>

<script setup>
import { Icon } from "@vicons/utils";
import { Link } from "@vicons/fa";
import { mainStore } from "@/store";
import { Swiper, SwiperSlide } from "swiper/vue";
import { Pagination, Mousewheel } from "swiper/modules";
import siteLinksData from "@/assets/siteLinks.json";

const store = mainStore();

// 当前选中的分类
const currentCategory = ref("home");

// 获取分类列表
const siteLinksCategories = computed(() => {
  return siteLinksData.categories || [];
});

// 获取当前分类下的网站链接
const currentLinks = computed(() => {
  const category = siteLinksCategories.value.find(c => c.id === currentCategory.value);
  return category ? category.items : [];
});

// 计算网站链接 - 每页 9 个（3排 x 3列）
const currentLinksList = computed(() => {
  const links = currentLinks.value;
  const result = [];
  for (let i = 0; i < links.length; i += 9) {
    const pageLinks = links.slice(i, i + 9);
    // 将每页的链接分成3排，每排3个
    const rows = [];
    for (let j = 0; j < pageLinks.length; j += 3) {
      rows.push(pageLinks.slice(j, j + 3));
    }
    result.push(rows);
  }
  return result;
});

// 切换分类
const switchCategory = (categoryId) => {
  currentCategory.value = categoryId;
};

// 链接跳转
const jumpLink = (data) => {
  if (data.name === "音乐" && store.musicClick) {
    if (typeof $openList === "function") $openList();
  } else {
    window.open(data.url, "_blank");
  }
};

onMounted(() => {
  console.log("Links loaded, categories:", siteLinksCategories.value.length);
});
</script>

<style lang="scss" scoped>
.links {
  .line {
    margin: 2rem 0.25rem 1rem;
    font-size: 1.1rem;
    display: flex;
    align-items: center;
    animation: fade 0.5s;
    .title {
      margin-left: 8px;
      font-size: 1.15rem;
      text-shadow: 0 0 5px #00000050;
    }
  }

  // 分类 Tabs
  .category-tabs {
    display: flex;
    gap: 8px;
    margin-bottom: 20px;
    flex-wrap: wrap;
    animation: fade 0.5s;

    .tab-item {
      padding: 8px 16px;
      border-radius: 20px;
      background: rgba(255, 255, 255, 0.1);
      color: #efefef;
      font-size: 0.9rem;
      cursor: pointer;
      transition: all 0.3s;
      border: 1px solid rgba(255, 255, 255, 0.2);
      white-space: nowrap;

      &:hover {
        background: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
      }

      &.active {
        background: rgba(255, 255, 255, 0.25);
        border-color: rgba(255, 255, 255, 0.5);
        font-weight: bold;
      }
    }
  }

  .swiper {
    left: -10px;
    width: calc(100% + 20px);
    padding: 5px 10px 0;
    z-index: 0;
    .swiper-slide {
      height: 100%;
      display: flex;
      flex-direction: column;
    }
    .swiper-pagination {
      margin-top: 12px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      :deep(.swiper-pagination-bullet) {
        background-color: #fff;
        width: 20px;
        height: 4px;
        margin: 0 4px;
        border-radius: 4px;
        opacity: 0.2;
        transition: opacity 0.3s;
        &.swiper-pagination-bullet-active {
          opacity: 1;
        }
        &:hover {
          opacity: 1;
        }
      }
    }
  }
  .link-row {
    margin-bottom: 20px;
  }
  .link-all {
    height: 100px;
    .item {
      height: 100px;
      width: 100%;
      display: flex;
      align-items: center;
      flex-direction: row;
      justify-content: center;
      padding: 0 10px;
      animation: fade 0.5s;

      &:hover {
        transform: scale(1.02);
        background: rgb(0 0 0 / 40%);
        transition: 0.3s;
      }

      &:active {
        transform: scale(1);
      }

      .site-icon {
        width: 26px;
        height: 26px;
        object-fit: contain;
        flex-shrink: 0;
      }

      .name {
        font-size: 1.1rem;
        margin-left: 8px;
      }
      @media (min-width: 720px) and (max-width: 820px) {
        .name {
          display: none;
        }
      }
      @media (max-width: 720px) {
        height: 80px;
      }
      @media (max-width: 460px) {
        flex-direction: column;
        .name {
          font-size: 1rem;
          margin-left: 0;
          margin-top: 8px;
        }
      }
    }
  }
}
</style>
