package com.example.simplemod;

import net.minecraft.core.BlockPos;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.monster.Spider;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.Blocks;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.material.Material;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraft.world.phys.HitResult;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.event.server.ServerStartingEvent;
import net.minecraftforge.eventbus.api.IEventBus;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.event.lifecycle.FMLClientSetupEvent;
import net.minecraftforge.fml.event.lifecycle.FMLCommonSetupEvent;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;

@Mod(SimpleMod.MODID)
public class SimpleMod {
    public static final String MODID = "simplemod";

    private static final DeferredRegister<Block> BLOCKS = DeferredRegister.create(ForgeRegistries.BLOCKS, MODID);
    private static final DeferredRegister<Item> ITEMS = DeferredRegister.create(ForgeRegistries.ITEMS, MODID);

    // Register the custom block
    public static final RegistryObject<Block> SPIDER_BLOCK = BLOCKS.register("spider_block",
            () -> new Block(BlockBehaviour.Properties.of(Material.STONE).strength(3.0f)) {
                @Override
                public void attack(BlockState state, Level world, BlockPos pos, net.minecraft.world.entity.player.Player player) {
                    if (!world.isClientSide()) {
                        // Spawn a spider on click (right click mechanics for server)
                        ServerLevel serverWorld = (ServerLevel) world;
                        Spider spider = EntityType.SPIDER.create(serverWorld);
                        if (spider != null) {
                            spider.moveTo(pos.getX() + 0.5, pos.getY() + 1, pos.getZ() + 0.5, 0.0F, 0.0F);
                            serverWorld.addFreshEntity(spider);
                        }
                    }
                }
            });

    public static final RegistryObject<Item> SPIDER_BLOCK_ITEM = ITEMS.register("spider_block",
            () -> new BlockItem(SPIDER_BLOCK.get(), new Item.Properties()));

    public SimpleMod() {
        IEventBus modEventBus = FMLJavaModLoadingContext.get().getModEventBus();
        BLOCKS.register(modEventBus);
        ITEMS.register(modEventBus);

        modEventBus.addListener(this::setup);
        MinecraftForge.EVENT_BUS.register(this);
    }

    private void setup(final FMLCommonSetupEvent event) {
        // Do something when the mod is being set up
    }

    @SubscribeEvent
    public void onServerStarting(ServerStartingEvent event) {
        // Do something when the server starts
    }
}
