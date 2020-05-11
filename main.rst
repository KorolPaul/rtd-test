# WoT FE ESLint config for Vue.js projects

=============================================
# Codestyle
## Стиль именования компонентов
* Имена файлов компонентов должны быть всегда в PascalCase.
```javascript
// bad
components/
    mycomponent.vue
    Mycomponent.vue
    myComponent.vue
    my-component.vue
 
// good
components/
    MyComponent.vue
    MySecondComponent.vue
```
* Имя компонента в шаблоне соответсвует имени файла импортируемого компонента и должно быть всегда в PascalCase.
```javascript
// bad
<template>
    <my-first-component />
    <myComponent />
    <mylastcomponent />
</template>
 
// good
<template>
    <MyFirstComponent />
    <MyComponent />
    <MyLastComponent />
</template>
```

## Секции в компонентах
Должен всегда использоваться один порядок для корневых тегов секций. Секция `<style>` не обязательна.
```javascript
// bad
<!-- Component1.vue -->
<script>/* ... */</script>
<template>...</template>
<style>/* ... */</style>
 
<!-- Component2.vue -->
<template>...</template>
<style>/* ... */</style>
<script>/* ... */</script>
 
// good
<!-- Component1.vue -->
<template>...</template>
<script>/* ... */</script>
<style>/* ... */</style>
 
<!-- Component2.vue -->
<template>...</template>
<script>/* ... */</script>
<style>/* ... */</style>
 
<!-- Component3.vue -->
<template>...</template>
<script>/* ... */</script>
```

## Закрытие тега компонента
* Компоненты без содержимого должны быть самозакрывающимися тегами.
```javascript
// bad
<template>
    <div class="page_glow"></div>
    <MyComponent></MyComponent>
    <span class="lvl"></span>
</template>
 
// good
<template>
    <div class="page_glow"/>
    <MyComponent />
    <span class="lvl"/>
</template>
```
* Вложенные компоненты всегда с новой строки 
```javascript
// bad
<template>
    <div class="page_glow"><MyComponent /></div>
</template>
 
// good
<template>
    <div class="page_glow">
        <MyComponent />
    </div>
</template>
```

## Атрибуты
### Форматирование
Атрибуты пишутся каждый с новой строки с выравниванием 4 пробела от тега родителя. 
Исключения: 
* Если атрибут один, то может (но не должен) оставаться на строке родителя.
* Если атрибутов ровно 2 и они короткие.
```javascript
// bad
<component v-if="isComponent" :prop1="someProp1" :prop2="someProp2" :prop3="true" @listener1="listenerHandler" @listener2="otherListenerHandler" v-seo-page:component/>
 
// maybe
<component
    v-if="isComponent"
/>
<component v-if="isComponent" :prop="true"/>
 
// good
<component v-if="isComponent"/>
<component
    v-if="isComponent"
    :prop="true"
/>
<component
    v-if="isComponent"
    :prop1="someProp1"
    :prop2="someProp2"
    :prop3="true"
    @listener1="listenerHandler"
    @listener2="otherListenerHandler"
    v-seo-page:component
/>
```
### Порядок
1. отпределение ( 'is' )
2. список ( 'v-for' )
3. условие ( 'v-if', 'v-else-if', 'v-show', 'v-cloak' )
4. модификатор отрисовки ( 'v-once', 'v-pre' )
5. id и class 
6. указатели ( 'ref', 'key', 'v-slot', 'slot' )
7. привязка к данным ('v-model')
8. другие атрибуты  компонента
9. props компонента
10. события ( @click )
11. содержимое ( 'v-html', 'v-text' )
12. директивы аналитики
13. перевод ( 'v-translate' )
```javascript
// bad
<component
    :prop1="someProp1"
    @listener1="listenerHandler"
    v-if="isComponent"
    :prop2="someProp2"
    v-seo-page:component
    :prop3="true"
    @listener2="otherListenerHandler"
/>
 
// good
<component
    v-if="isComponent"
    :prop1="someProp1"
    :prop2="someProp2"
    :prop3="true"
    @listener1="listenerHandler"
    @listener2="otherListenerHandler"
    v-seo-page:component
/>
```

### class и :class
Разделяем статические и динамичесские классы.
```javascript
// bad
<component
    :class="[
		'some-class'
		`some-class_${dynamic}`,
        {[`some-class_${otherDynamic}`]: otherDynamic },
        {'some-class__active': isActive }
    ]"
/>

// good
<component
    class="some-class"
	:class="[
		`some-class_${dynamic}`,
        {[`some-class_${otherDynamic}`]: otherDynamic },
        {'some-class__active': isActive }
    ]"
/>
```

### Закрываюший тег:
Закрывающий тег в многострочном компоненте выравнивается с открывающимся.
```javascript
// bad
<div>
    <component
        v-if="isComponent"
        :prop1="someProp1"
        :prop2="someProp2"
        :prop3="true"
        @listener1="listenerHandler"
        @listener2="otherListenerHandler"
        v-seo-page:component />
</div>
 
// good
<div>
    <component
        v-if="isComponent"
        :prop1="someProp1"
        :prop2="someProp2"
        :prop3="true"
        @listener1="listenerHandler"
        @listener2="otherListenerHandler"
        v-seo-page:component
    />
</div>
```