<template>
    <div class="row">
        <div class="dial-col col-lg-6">
            <!-- <div id="circleColour"></div> -->
            <div id='container'>
                <div id='slider'>
                </div>
            </div>
            <div class="my-auto user-select-none">{{ time.hours }}h {{ time.minutes }}m</div>

        </div>
        <div class="col-lg-6">
            <h6>Your parking untill:</h6>
            <p>11/1 10:30</p>
            <hr>
            <h6>Price:</h6>
            <p>{{ price }} DKK</p>
            <hr>
            <h6>Car:</h6>
            <p>{{ car.licenseplate }} - {{ car.brand }} {{ car.model }}</p>
            <hr>
            <h6>Area:</h6>
            <p>{{ area.address }}</p>
        </div>
    </div>

</template>
<script>
export default {
    name: "TimeDial",
    data() {
        return {
            current: 0,
            time: {
                hours: 0,
                minutes: 0
            },
            price: 0,
            parkingUntil: "No Time Selecte"
        };
    },
    props: {
        area: {
            type: Object,
        },
        car: {
            type: Object,
        }
    },

    methods: {
        mod(x, n) {
            return ((x % n) + n) % n;
        },
        getOffset(containerElement, offsetType) {
            let parents = [];
            this._getParents(containerElement, parents)

            let offsetSum = 0;
            for (let i = 0; i < parents.length; i++) {
                offsetSum += parents[i][offsetType];
            }
            return offsetSum + 150;
        },
        _getParents(element, list) {
            // Get all parent elements and push them to the list
            if (element.parentElement) {
                // Exclude body and html
                // if (element.parentElement.tagName == 'BODY' || element.parentElement.tagName == 'HTML') {
                //     return;
                // }
                list.push(element.parentElement);
                this._getParents(element.parentElement, list);
            }
        },
    },
    watch: {
        'current': function(value){
            let minutes = value / 6
            const date = new Date().toJSON().slice(0,10).replace(/-/g,'/');
            this.time.hours = Math.floor(minutes / 60);
            this.time.minutes = Math.round(minutes % 60);
            this.price = minutes * 0.15
            this.parkingUntil = date
        }
    },
    mounted() {
        console.log(this.car)
        console.log(this.area)
        // DIAL SLIDER: https://stackoverflow.com/questions/20505132/javascript-circle-slider-degrees-to-time
        // let counter = 0;
        var lastAngle = 0;

        let container = document.querySelector('#container');
        let $slider = document.querySelector('#slider');
        // let sliderW2 = $slider.clientWidth / 2;
        // let sliderH2 = $slider.clientHeight / 2;
        let sliderW2 = 20;
        let sliderH2 = 20;
        let radius = 100;
        let deg = 0;
        let elPLeft = this.getOffset(container, 'offsetLeft');
        let elPTop = this.getOffset(container, 'offsetTop');
        let elPos = { x: elPLeft, y: elPTop }; // Element intial position
        // console.log('elPos: ', elPos)
        // console.log('sliderW2: ', sliderW2)
        // console.log('sliderH2: ', sliderH2)
        let X = 0, Y = 0;
        let mdown = false;
        document.querySelector('#container').addEventListener('mousedown', () => { mdown = true; })
        document.querySelector('#container').addEventListener('touchstart', () => { mdown = true; })
        document.addEventListener('mouseup', () => { mdown = false; })
        // document.addEventListener('touchend', () => { mdown = false; })
        document.querySelector('#container').addEventListener('mousemove', (e) => {
            if (mdown) {
                let mPos = { x: e.clientX - elPos.x, y: e.clientY - elPos.y };
                let atan = Math.atan2(mPos.x - radius, mPos.y - radius);
                deg = -atan / (Math.PI / 180) + 180; // final (0-360 positive) degrees from mouse position 

                
                // console.log('e.client: ', e.clientX + '  *  ' + e.clientY + '\nmPos: ', mPos + '\ndeg: ', deg);
                

                X = Math.round(radius * Math.sin(deg * Math.PI / 180));
                Y = Math.round(radius * -Math.cos(deg * Math.PI / 180));
                // $slider.style.({ left: X + radius - sliderW2, top: Y + radius - sliderH2 });
                $slider.style.left = X + radius - sliderW2 + 'px';
                $slider.style.top = Y + radius - sliderH2 + 'px';

                // AND FINALLY apply exact degrees to ball rotation
                $slider.style.transform = 'rotate(' + deg + 'deg)';
                // $slider.style.WebkitTransform = 'rotate(' + deg + 'deg)';
                // $slider.style.-moz-transform = 'rotate(' + deg + 'deg)';

                let delta = 0;
                let dir = 0;
                let rawDelta = this.mod(deg - lastAngle, 360.0);
                if (rawDelta < 180) {
                    dir = 1;
                    delta = rawDelta;
                } else {
                    dir = -1;
                    delta = rawDelta - 360.0;
                }

                if (!dir) {
                    // console.log();
                }


                this.current += delta;
                lastAngle = deg;
                if (this.current < 0) {
                    this.current = 0;
                    $slider.style.top = -20 + 'px';
                    $slider.style.left = 80 + 'px';
                    $slider.style.transform = 'rotate(' + 0 + 'deg)';
                    return;
                }

                // this.time = this.getReadableTime(current / 6);
            }
        });
        // document.querySelector('#container').addEventListener('touchmove', (e) => { // mousemove
        //     console.log(e);
        //     if (mdown) {
        //         let mPos = { x: e.touches[0].screenX - elPos.x, y: e.touches[0].screenY - elPos.y };
        //         let atan = Math.atan2(mPos.x - radius, mPos.y - radius);
        //         deg = -atan / (Math.PI / 180) + 180; // final (0-360 positive) degrees from mouse position 

                
        //         // console.log('e.client: ', e.clientX + '  *  ' + e.clientY + '\nmPos: ', mPos + '\ndeg: ', deg);
                

        //         X = Math.round(radius * Math.sin(deg * Math.PI / 180));
        //         Y = Math.round(radius * -Math.cos(deg * Math.PI / 180));
        //         // $slider.style.({ left: X + radius - sliderW2, top: Y + radius - sliderH2 });
        //         $slider.style.left = X + radius - sliderW2 + 'px';
        //         $slider.style.top = Y + radius - sliderH2 + 'px';

        //         // AND FINALLY apply exact degrees to ball rotation
        //         $slider.style.transform = 'rotate(' + deg + 'deg)';
        //         // $slider.style.WebkitTransform = 'rotate(' + deg + 'deg)';
        //         // $slider.style.-moz-transform = 'rotate(' + deg + 'deg)';

        //         let delta = 0;
        //         let dir = 0;
        //         let rawDelta = this.mod(deg - lastAngle, 360.0);
        //         if (rawDelta < 180) {
        //             dir = 1;
        //             delta = rawDelta;
        //         } else {
        //             dir = -1;
        //             delta = rawDelta - 360.0;
        //         }

        //         if (!dir) {
        //             // console.log();
        //         }


        //         this.current += delta;
        //         lastAngle = deg;
        //         if (this.current < 0) {
        //             this.current = 0;
        //             $slider.style.top = -20 + 'px';
        //             $slider.style.left = 80 + 'px';
        //             $slider.style.transform = 'rotate(' + 0 + 'deg)';
        //             return;
        //         }

        //         // this.time = this.getReadableTime(current / 6);
        //     }
        // });
    },

};
</script>
<style scoped>
/* .dial-container {
    display: flex !important;
    align-content: space-around;
    justify-content: space-around;
    height: 300px;
    width: 300px;
} */

.dial-col {
    display: flex;
    justify-content: center;
    align-items: center;
}

#container {
    position: absolute;
    width: 200px;
    height: 200px;
    /* background: #999; */
    border: 5px solid #5e5e5e;
    border-radius: 1000px;
}

#circleColour {
    position: absolute;
    width: 200px;
    height: 200px;
    border: 5px solid #d8956a;
    top: 50px;
    left: 50px;
    border-radius: 50%;
    /* z-index: 999; */
}

#slider {
    position: relative;
    height: 30px;
    width: 30px;
    left: 90px;
    top: -20px;
    background: black no-repeat center 20px;
    border-radius: 20px;
}
</style>