<template>
  <div class="more-content">
    <textarea
      v-model="content"
      placeholder="您可在此编写任意内容..."
      class="custom-textarea"
      @input="saveContent"
    />
  </div>
</template>

<script setup>
// 从 localStorage 读取保存的内容
const savedContent = localStorage.getItem('moreContent') || '';
const content = ref(savedContent);

// 保存内容到 localStorage
const saveContent = () => {
  localStorage.setItem('moreContent', content.value);
};
</script>

<style lang="scss" scoped>
.more-content {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  width: 100%;
  flex: 1;

  .custom-textarea {
    width: 100%;
    height: 100%;
    min-height: 150px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 8px;
    padding: 15px;
    color: #efefef;
    font-size: 0.95rem;
    line-height: 1.6;
    resize: none;
    outline: none;
    transition: all 0.3s;

    &::placeholder {
      color: rgba(239, 239, 239, 0.5);
    }

    &:focus {
      background: rgba(255, 255, 255, 0.15);
      border-color: rgba(255, 255, 255, 0.4);
    }
  }
}
</style>
