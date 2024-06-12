<template>
        <div class="flex flex-col min-h-screen">
            <main class="flex-grow">
                <!-- Content goes here -->
            </main>
            <footer class="bg-gray-800 text-white py-4 PiePagina">
                <div class="container mx-auto text-center">
                    <p>&copy; 2023 My Website. All rights reserved.</p>
                </div>
            </footer>
        </div>

</template>

<style>
.PiePagina {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    background-color: rgb(51, 51, 51);
    z-index: 999;
}
</style>