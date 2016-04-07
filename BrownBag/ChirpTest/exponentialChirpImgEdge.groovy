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

import net.imglib2.FinalInterval;
import net.imglib2.RandomAccessibleInterval;
import net.imglib2.util.Intervals;
import net.imglib2.view.Views;

exponentialChirp=ops.create().img(new FinalDimensions(512,512),new FloatType())
noisyChirp=ops.create().img(new FinalDimensions(512,512),new FloatType())

FinalInterval interval = Intervals.createMinMax( 128, 128, 384, 384 );
RandomAccessibleInterval region = Views.interval( exponentialChirp, interval );

formula = "500 * (Math.sin(2*Math.PI*0.1*Math.pow(4.5,p[0]/149.8)*p[0]/149.8 )+1)+1"
ops.image().equation(region, formula)
ui.show(exponentialChirp)

IJ.resetMinAndMax();
IJ.makeLine(0, 256, 511, 256);
IJ.run("Plot Profile");

IJ.run("Diffraction PSF 3D", "index=1.520 numerical=1.42 wavelength=510 "
+ "longitudinal=0 image=10 slice=200 width,=512 height,=512 depth,=1 "
+ "normalization=[Sum of pixel values = 1] title=PSF");

psf=IJ.getImage()
psf=ImageJFunctions.wrapFloat(psf)

convolved=ops.filter().convolve(exponentialChirp, psf)
ui.show(convolved)

IJ.resetMinAndMax();
IJ.makeLine(0, 256, 511, 256);
IJ.run("Plot Profile");

noisy=ops.filter().addPoissonNoise(noisyChirp,convolved)
//print "noisy is:",noisy
ui.show("noisy",noisy)
IJ.resetMinAndMax();
IJ.makeLine(0, 256, 511, 256);
IJ.run("Plot Profile");

IJ.run("Iterative Deconvolve 3D", "image=noisy point=PSF "
+ "output=Deconvolved normalize show log perform wiener=0.33 "
+ "low=0 z_direction=1 maximum=200 terminate=0.001");

IJ.resetMinAndMax();
IJ.makeLine(0, 256, 511, 256);
IJ.run("Plot Profile");
