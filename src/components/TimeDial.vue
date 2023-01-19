<template>
    <div class="container dial-container">
        <!-- <div id="circleColour"></div> -->
        <div id='container'>
            <div id='slider'>
            </div>
        </div>

        <div id="timeDisplay" class="my-auto user-select-none">
        </div>

    </div>

</template>
<script>
export default {
    name: "TimeDial",
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
        getReadableTime(minutes) {
            // Convert minutes to readable time format - Don't include hours if 0
            let hours = Math.floor(minutes / 60);
            let minutesLeft = Math.round(minutes % 60);
            let readableTime = hours + 'h ' + minutesLeft + 'm';
            return readableTime;
        },
    },
    mounted() {
        // DIAL SLIDER: https://stackoverflow.com/questions/20505132/javascript-circle-slider-degrees-to-time
        let counter = 0;
        var current = 0;
        var lastAngle = 0;
        // const $ = document.querySelector();

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
        let elPos = { x: elPLeft, y: elPTop };
        // let elPos = { x: 50, y: 50 };
        // console.log('elPos: ', elPos)
        // console.log('sliderW2: ', sliderW2)
        // console.log('sliderH2: ', sliderH2)
        let X = 0, Y = 0;
        let mdown = false;
        document.querySelector('#timeDisplay').innerHTML = this.getReadableTime(current / 6);
        document.querySelector('#container').addEventListener('mousedown', () => { mdown = true; })
        document.addEventListener('mouseup', () => { mdown = false; })
        document.querySelector('#container').addEventListener('mousemove', (e) => {
            if (mdown) {
                let mPos = { x: e.clientX - elPos.x, y: e.clientY - elPos.y };
                let atan = Math.atan2(mPos.x - radius, mPos.y - radius);
                deg = -atan / (Math.PI / 180) + 180; // final (0-360 positive) degrees from mouse position 

                if (counter % 100 == 0) {
                    // console.log('e.clientX: ', e.clientX);
                    // console.log('e.clientY: ', e.clientY);
                    // console.log('mPos: ', mPos);
                    // console.log('deg: ', deg);
                }

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
                

                current += delta;
                lastAngle = deg;
                if (current < 0) {
                    current = 0;
                    $slider.style.top = -20 + 'px';
                    $slider.style.left = 80 + 'px';
                    $slider.style.transform = 'rotate(' + 0 + 'deg)';
                    return;
                }

                document.querySelector('#timeDisplay').innerHTML = this.getReadableTime(current / 6);
                counter++;
            }
        });

    },

};
</script>
<style scoped>

.dial-container {
    display: flex!important;
    align-content: space-around;
    justify-content: space-around;
    height: 300px;
    width: px;
    /* top: -50px; */
    /* border: 1px solid #999; */
}
#container {
    position: absolute;
    top: 50px;
    left: 50px;
    width: 200px;
    height: 200px;
    background: #999;
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