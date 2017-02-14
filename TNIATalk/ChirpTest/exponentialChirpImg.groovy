// @OpService ops
// @UIService ui
// @ConvertService convert
// @DatasetService data

import ij.IJ;
import net.imglib2.FinalDimensions
import net.imglib2.type.numeric.real.FloatType
import net.imagej.ImgPlus
import net.imglib2.img.Img
import net.imglib2.img.display.imagej.ImageJFunctions


blank=ops.create().img(new FinalDimensions(512,512),new FloatType())
noisy=ops.create().img(new FinalDimensions(512,512),new FloatType())

formula = "50 * (Math.sin(2*Math.PI*0.1*Math.pow(3,p[0]/149.8)*p[0]/149.8 )+1)+1"
exponentialChirp = ops.image().equation(blank, formula)
ui.show(exponentialChirp)

IJ.resetMinAndMax();
IJ.makeLine(0, 32, 511, 32);
IJ.run("Plot Profile");

IJ.run("Diffraction PSF 3D", "index=1.520 numerical=1.42 wavelength=510 "
+ "longitudinal=0 image=10 slice=200 width,=512 height,=512 depth,=1 "
+ "normalization=[Sum of pixel values = 1] title=PSF");

psf=IJ.getImage()

print "psf if: "+psf
//psf=convert.convert(psf, ImgPlus.class)
psf=ImageJFunctions.wrapFloat(psf)
print "psf if: "+psf

convolved=ops.filter().convolve(exponentialChirp, psf)
ui.show(convolved)

IJ.resetMinAndMax();
IJ.makeLine(0, 32, 511, 32);
IJ.run("Plot Profile");

noisy=ops.filter().addPoissonNoise(noisy,convolved)
//print "noisy is:",noisy
ui.show(noisy)

deconvolved=ops.deconvolve().richardsonLucy(noisy, psf,10)
ui.show("deconvolved", deconvolved)

