<template>
    <div class="col-xl-6">

    </div>
    <div>

    </div>
    <div class="container mt-5">
        <div class="action-prompt m-auto">
            <h3 class="text-center">NEW CAR</h3>
            <hr>
            <form>
                <input id="plateImage" type="file" accept="image/*" />
                <p>Simply scan your car's license plate, and have it registered automatically!</p>
                <button class="btn btn-primary btn-dark" @click="getPlate">SCAN NUMBER PLATE</button>
                <img id="previewImg" src="" width="200" />

                <p>Or manually input the info here:</p>
                <label for="numberPlate">Number plate</label>
                <br />
                <input name="numberPlate" id="numberPlate" type="text" pattern="[A-Z]{2}[0-9]{5}"
                    title="Please follow Danish number plate structure" />

                <br />

                <input type="submit" value="Submit" />
            </form>
        </div>
    </div>
</template>

<script>
const fileTypes = [
    "image/apng",
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/pjpeg",
    "image/png",
    "image/svg+xml",
    "image/tiff",
    "image/webp",
    "image/x-icon"
];

function validFileType(file) {
    return fileTypes.includes(file.type);
}

export default {
    methods: {
        getPlate(event) {
            try {
                const picture = document.getElementById("plateImage");
                console.log(picture);

                if (picture.value != '') {
                    const curFiles = picture.files;
                    console.log(curFiles);
                    if (curFiles.length === 0) {
                        console.log("No files currently selected for upload");
                    }
                    else {
                        for (const file of curFiles) {
                            if (validFileType(file)) {
                                let img = document.getElementById("previewImg");
                                img.src = URL.createObjectURL(file);
                                console.log(file);
                            } else {
                                console.log("NOT A VALID FILE");
                            }
                        }
                    }
                } else {
                    alert("Please select a picture of your number plate")
                }

            } catch (error) {
                console.log('Input picture: ' + error)
            }

            console.log(event.target.name);
        }
    }
}
</script>


<style scoped>
.action-prompt {
    border: 1px solid white;
    border-radius: 12px;
    padding: 15px;
    height: 50%;
    width: 50%;
    position: relative;
    background: rgba(0, 0, 0, 0.4);
}

.btn-transparent {
    background: transparent;
    color: white;
    border-color: white;
}

.btn-transparent:hover {
    background: white;
    color: black;
}

.form-floating>.label {
    color: black !important;
}
</style>

